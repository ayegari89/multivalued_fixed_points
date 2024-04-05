class ProgressReporter():
    def __init__(self, progress_bar):
        self.progress_bar =progress_bar

    def report(self, value):
        self.progress_bar.setValue(value)
        self.progress_bar.repaint()

