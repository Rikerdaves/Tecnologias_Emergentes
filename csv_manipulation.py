import csv
from statistics import mean

class dataset:
    def __init__(self, filename):
        self.filename = filename
        self.csv_file = []

    #Metodo ler arquivo csv
    def load_from_csv(self):

        with open(self.filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)

            for row in reader:
                self.csv_file.append(row)
        return self.csv_file
    
    #metodo para calcular valor total de uma coluna
    def total_from_csv(self, col_index, row_number):

        with open(self.filename) as csvfile:
            reader = csv.reader(csvfile)

            # índice da coluna desejada (por exemplo, a segunda coluna):
            col_index = int(col_index)

            # número da linha desejada (por exemplo, a terceira linha):
            row_number = int(row_number)

            # loop através do arquivo CSV para encontrar a célula desejada:
            for i, row in enumerate(reader):
                if i == row_number - 1:  # encontrou a linha desejada
                    cell_value = row[col_index]
                    print(f'valor total {cell_value}: ')

                    break

            #criar uma lista dos valores na coluna desejada:
            col_values = [float(row[col_index]) for row in reader]

            #calcular a soma dos valores na coluna:
            col_sum = sum(col_values)

            print(f'{col_sum}: ')

    #metodo para calcular valor da media de uma coluna
    def media_from_csv(self, col_index, row_number):
        with open(self.filename) as csvfile:
            reader = csv.reader(csvfile)

            # índice da coluna desejada (por exemplo, a segunda coluna):
            col_index = int(col_index)

            # número da linha desejada (por exemplo, a terceira linha):
            row_number = int(row_number)

            # loop através do arquivo CSV para encontrar a célula desejada:
            for i, row in enumerate(reader):
                if i == row_number - 1:  # encontrou a linha desejada
                    cell_value = row[col_index]
                    print(f'valor da média {cell_value}: ')

                    break


        with open(self.filename) as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header row

            # índice da coluna desejada
            col_index = int(col_index)

            # criar uma lista dos valores na coluna desejada
            col_values = [float(row[col_index]) for row in reader]

            # calcular a média dos valores na coluna
            col_mean = mean(col_values)

            print(f'{col_mean:.2f}')
        
#Objetos da classe dataset:
drinks = dataset('drinks.csv')#Alterar diretório do csv em caso de erro!

if __name__ == '__main__':
    print(drinks.load_from_csv())
    drinks.total_from_csv(1, 1)#Passar o índice da coluna e o número da linha
    drinks.media_from_csv(1,1)#passar o índice da coluna e o número da linha

        