import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit
from PyQt5.QtWidgets import QLineEdit, QTableWidget, QTableWidgetItem, \
    QHBoxLayout, QInputDialog, QMessageBox, QProgressBar

import barvinok
from progress_reporter import ProgressReporter


class HelpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Help')

        layout = QVBoxLayout()

        # Add a QLabel to display LaTeX formulas as GIF images
        self.formula_label = QLabel()
        self.formula_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.formula_label)

        # Add a button to close the window
        self.close_button = QPushButton('Close')
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)

        self.setLayout(layout)

        # Load and display help content
        self.display_latex_formula()

    def display_latex_formula(self):
        # Load the GIF image of the LaTeX formula
        gif_path = './help_windows.png'  # Replace with the path to your GIF image
        movie = QMovie(gif_path)
        self.formula_label.setMovie(movie)
        movie.start()


class MatrixProcessorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create widgets
        self.matrix_label = QLabel("Matrix:")
        self.entry_matrix = QTableWidget(self)
        self.m_label = QLabel("Enter Integer m:")
        self.entry_m = QLineEdit(self)
        self.entry_m.setMaximumWidth(50)
        self.number_of_rows_label = QLabel("Enter number of rows")
        self.number_of_rows = QLineEdit(self)
        self.number_of_rows.setMaximumWidth(50)

        self.submit_button = QPushButton("Submit", self)
        self.result_label = QTextEdit("")
        self.result_label.setReadOnly(True)
        self.result_label.setFont(QFont('Arial', 20))

        # Loading animation
        self.loading_bar = QProgressBar(self)
        self.loading_bar.setAlignment(Qt.AlignCenter)
        self.loading_bar.setVisible(False)
        # Set up layout
        matrix_layout = QVBoxLayout()
        matrix_layout.addWidget(self.matrix_label)
        matrix_layout.addWidget(self.entry_matrix)

        help_button_layout = QHBoxLayout()
        #self.old_buttons(help_button_layout)

        help_button = QPushButton("Help", self)
        help_button.setToolTip("Help (Ctrl+H)")
        help_button.setShortcut("Ctrl+H")
        help_button.clicked.connect(self.open_help_window)
        help_button_layout.addWidget(help_button)
        input_rows_layout = QVBoxLayout()

        input_rows_layout.addWidget(self.number_of_rows_label)
        input_rows_layout.addWidget(self.number_of_rows)

        input_m_layout = QVBoxLayout()
        input_m_layout.addWidget(self.m_label)
        input_m_layout.addWidget(self.entry_m)

        main_layout = QVBoxLayout(self)
        main_layout.addLayout(input_m_layout)
        main_layout.addLayout(input_rows_layout)

        main_layout.addLayout(matrix_layout)

        main_layout.addWidget(self.submit_button)
        main_layout.addWidget(self.result_label)
        main_layout.addWidget(self.loading_bar)
        main_layout.addLayout(help_button_layout)

        self.setLayout(main_layout)

        # Connect the button click event to the on_submit method
        self.submit_button.clicked.connect(self.on_submit)

        # Connect the itemChanged signal to the on_matrix_item_changed method
        self.entry_matrix.itemChanged.connect(self.on_matrix_item_changed)

        self.number_of_rows.editingFinished.connect(self.number_of_rows_changed)

        # Set up the main window
        self.setWindowTitle("Fixed points of MV networks")
        self.setGeometry(100, 100, 800, 400)

        self.help_window = HelpWindow()
        self.show()

    def old_buttons(self, button_layout):
        add_row_button = QPushButton("Add Row", self)
        add_row_button.setToolTip("Add Row (Ctrl+R)")
        add_row_button.setShortcut("Ctrl+R")
        add_row_button.clicked.connect(self.add_row)
        button_layout.addWidget(add_row_button)
        remove_row_button = QPushButton("Remove Row", self)
        remove_row_button.setToolTip("Remove Row (Ctrl+Shift+R)")
        remove_row_button.setShortcut("Ctrl+Shift+R")
        remove_row_button.clicked.connect(self.remove_row)
        button_layout.addWidget(remove_row_button)
        add_col_button = QPushButton("Add Column", self)
        add_col_button.setToolTip("Add Column (Ctrl+C)")
        add_col_button.setShortcut("Ctrl+C")
        add_col_button.clicked.connect(self.add_column)
        button_layout.addWidget(add_col_button)
        remove_col_button = QPushButton("Remove Column", self)
        remove_col_button.setToolTip("Remove Column (Ctrl+Shift+C)")
        remove_col_button.setShortcut("Ctrl+Shift+C")
        remove_col_button.clicked.connect(self.remove_column)
        button_layout.addWidget(remove_col_button)

    def open_help_window(self):
        self.help_window.show()

    def add_row(self):
        current_rows = self.entry_matrix.rowCount()
        self.entry_matrix.setRowCount(current_rows + 1)

        for col in range(self.entry_matrix.columnCount()):
            item = QTableWidgetItem("0")
            item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.entry_matrix.setItem(current_rows, col, item)

    def remove_row(self):
        current_rows = self.entry_matrix.rowCount()
        if current_rows > 1:
            self.entry_matrix.setRowCount(current_rows - 1)

    def add_column(self):
        current_cols = self.entry_matrix.columnCount()
        self.entry_matrix.setColumnCount(current_cols + 1)

        for row in range(self.entry_matrix.rowCount()):
            item = QTableWidgetItem("0")
            item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.entry_matrix.setItem(row, current_cols, item)

    def remove_column(self):
        current_cols = self.entry_matrix.columnCount()
        if current_cols > 1:
            self.entry_matrix.setColumnCount(current_cols - 1)

    def process_input(self, matrix, m):
        n = matrix.shape[0]
        # Show loading animation
        self.loading_bar.setRange(0, 2 ** n)  # Setting range to (0, 0) creates an infinite progress bar
        self.loading_bar.setVisible(True)
        self.loading_bar.repaint()
        # Start processing in a separate thread
        result = barvinok.compute_steady_states_barvinok(matrix, n, m, ProgressReporter(self.loading_bar))

        return result

    def on_submit(self):
        matrix = self.get_matrix_values()
        integer2 = self.validate_integer_input(self.entry_m.text())

        if matrix is None or integer2 is None:
            self.show_error("""Only integer numbers are accepted,
                                   or fractions with m as denominator in last column of the matrix.""")
            return

        result = self.pretty_print_result(integer2, self.process_input(np.array(matrix), integer2))
        self.result_label.setText(f"{result}")
        self.loading_bar.setVisible(False)

    def pretty_print_result(self, m, result):
        if not result:
            return "There are no solutions"
        elif len(result) == 1:
            return f"There is 1 solution: ({self.pretty_print(m, result[0])})"
        else:
            return f"There are {len(result)} solutions: <ul> {' '.join(f'<li>({self.pretty_print(m, sol)})</li>' for sol in result)}</ul>"

    def pretty_print(self, m, solution):
        return ", ".join(self.pretty_print_element(m, element) for element in solution.split(","))

    def pretty_print_element(self, m, element):
        if int(element) == 0:
            return "0"
        elif int(element) == m:
            return "1"
        else:
            return f"{element}/{m}"

    def on_matrix_item_changed(self, item):
        # Update the value of the matrix item when changed
        if not self.validate_matrix_item(item):
            self.show_invalid_input_message()

    def number_of_rows_changed(self):
        text = self.number_of_rows.text()
        if not self.is_valid_integer(text):
            self.show_error("Please enter valid integers.")
            self.number_of_rows.setText(str(self.entry_matrix.rowCount()))
            return False
        self.entry_matrix.setRowCount(0)
        self.entry_matrix.setColumnCount(0)
        for row in range(self.rows()):
            self.add_row()
            self.add_column()
        self.add_column()
        return True

    def rows(self):
        return int(self.number_of_rows.text())

    def validate_matrix_item(self, item):
        # Validate and update the matrix item content
        text = item.text()
        if item.column() != self.rows() and not self.is_valid_integer(text):
            item.setText("0")
            return False
        if item.column() == self.rows() and not self.is_valid_fraction_or_integer(text):
            return False
        return True

    def get_matrix_values(self):
        matrix_values = []
        for row in range(self.entry_matrix.rowCount()):
            row_values = []
            for col in range(self.entry_matrix.columnCount()-1):
                item_text = self.entry_matrix.item(row, col).text()
                if not self.is_valid_integer(item_text):
                    return None
                row_values.append(int(item_text))
            item_text = self.entry_matrix.item(row, self.entry_matrix.columnCount()-1).text()
            if not self.is_valid_fraction_or_integer(item_text):
                return None
            if self.is_valid_integer(item_text):
                row_values.append(int(item_text) * int(self.entry_m.text()))
            else:
                row_values.append(int(item_text.split("/")[0]))
            matrix_values.append(row_values)
        return matrix_values

    def validate_integer_input(self, text):
        if not self.is_valid_integer(text):
            return None
        return int(text)

    def is_valid_integer(self, text):
        try:
            int(text)
            return True
        except ValueError:
            return False

    def is_valid_fraction_or_integer(self, text):
        if self.is_valid_integer(text):
            return True

        a = text.split("/")
        if len(a)!=2:
            return False
        if not self.is_valid_integer(a[0]):
            return False
        if not self.is_valid_integer(a[1]):
            return False
        if int(a[1]) != int(self.entry_m.text()):
            return False
        return True


    def show_error(self, message):
        self.show_invalid_input_message(message)
        #return
        #error_dialog = QLabel(self)
        #error_dialog.setInputMode(QLabel.TextInput)
        #error_dialog.setWindowTitle("Error")
        #error_dialog.setLabelText(message)
        #error_dialog.exec_()

    def show_invalid_input_message(self,
                                   message="""Only integer numbers are accepted in the matrix,
                                   or fractions with m as denominator in last column."""):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText(message)
        msg_box.setWindowTitle("Invalid Input")
        msg_box.exec_()


if __name__ == '__main__':
    app = QApplication([])
    window = MatrixProcessorApp()
    app.exec_()
