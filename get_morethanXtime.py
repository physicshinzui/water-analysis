#!/Users/siida/anaconda3/bin/python
import sys

def main():
    filename = sys.argv[1]
    with open(filename) as fin:
        py_sele = []
        for i, line in enumerate(fin):
            index, tau = str(line.split(',')[0]), int(line.split(',')[1])
            if tau > 30: 
                py_sele.append(index)
    
    sele = 'sele id ' + '+'.join(py_sele)
    print(sele)

if __name__ == "__main__":
    import doctest
    main()
    