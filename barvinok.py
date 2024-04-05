import subprocess
import sys
import gmpy2

def correr_instancia(archivo):
    with open(archivo, "r") as input:
        proc = subprocess.Popen(["./barvinok/polytope_scan"], stdin=input, stdout=subprocess.PIPE, close_fds=False)
        output = proc.stdout.read().decode("utf-8")
        return output.split('\n')[:-1]


# TODO: generalizar para que se puedan pasar los parametros c1,c2, ..cn
def guardar_instancia(M, n, m, subset):
    file_name = '/tmp/instancia_%s_%s.txt' % (n, m)
    len_subset = gmpy2.popcount(subset)
    with open(file_name, 'w+') as output_file:
        output_file.write(str(2 * n + len_subset) + ' ' + str(n + 2) + '\n')
        A = []
        b = []
        c = []
        # construyo x=0 para lo que no esta en subset
        for j in range(n):
            # if j not in subset:
            if subset & (1 << j) == 0:
                # condicion x_j=0
                l_j0 = [0] * n
                l_j0[j] = -1
                A.append(l_j0)
                b.append([0])
                c.append([0])
        # construyo x>=1 y x<=m para el subset
        for j in range(n):
            # if j in subset:
            if subset & (1 << j) != 0:
                # condicion x_j>0
                l_j0 = [0] * n
                l_j0[j] = 1
                A.append(l_j0)
                l_jm = [0] * n
                l_jm[j] = -1
                A.append(l_jm)
                b.append([-1])
                b.append([m])
                c.append([1])
                c.append([1])
        # construyo Mx+c<=0 para lo que no esta en el subset
        # Mx<=-c en este caso A =-M
        for j in range(n):
            # if j not in subset:
            if subset & (1 << j) == 0:
                l_j = [-M[j][s] for s in range(n)]
                A.append(l_j)
                # multiplico por m para encontrar las soluciones enteras del sistema.
                # (asumimos que c* viene mmultiplicada por m pora evitar problemas de precision)
                b.append([int(-M[j][-1])])
                c.append([1])

        # armamos el sistema a resolver Ax +b=x <-> (A-I)x = -b
        # (M-I)x=b para los casos del subset
        # en este caso A= -(M-I) = I- M
        for j in range(n):
            # if j in subset:
            if subset & (1 << j) != 0:
                l_j = [-M[j][s] if j != s else -M[j][s] + 1 for s in range(n)]
                A.append(l_j)
                # multiplico por m para encontrar las soluciones enteras del sistema.
                # (asumimos que c* viene mmultiplicada por m pora evitar problemas de precision)
                b.append([int(-M[j][-1])])
                c.append([0])

        for i in range(len(A)):
            output_file.write(str(c[i][0]) + ' ')
            for j in range(n - 1):
                output_file.write(str(A[i][j]) + ' ')
            output_file.write(str(A[i][n - 1]) + ' ' + str(b[i][0]) + '\n')
    return file_name


def compute_steady_states_for_subset(M, n, m, subset):
    ejemplo = guardar_instancia(M, n, m, subset)
    res = correr_instancia(ejemplo)
    return res


# algoritmo 2
def compute_steady_states_barvinok(M, n, m, reporter=None):
    # Paso1: i es un nro entre 0 y 2^n, es decir todos los posibles subconjuntos de n elementos(es para armar las regiones R_I)
    res = []
    for i in range(1 << n):
        if i % 100 == 0 and reporter is not None:
            reporter.report(i)
        solucion_parcial = compute_steady_states_for_subset(M, n, m, i)
        res += solucion_parcial

    return res

def main(parametros):
    if len(parametros) != 4:
        return compute_steady_states_barvinok(eval(parametros[1]), int(parametros[2]), int(parametros[3]))
    raise ValueError("3 parameters should be sent to the program")

if __name__ == '__main__':
    r = main(sys.argv)
    print(r)
