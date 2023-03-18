import pandas as pd

class CSVFile:
    def __init__(self, filename):
        self.filename = filename
        self.columns = []
        self.data = pd.read_csv(filename)
        
        for column_name in self.data.columns:
            column_values = self.data[column_name].tolist()
            self.add_column(column_name, column_values)
        
    def add_column(self, name, values):
        column = CSVColumn(name, values)
        self.columns.append(column)
        
    def remove_column(self, name):
        self.columns = [c for c in self.columns if c.name != name]
        self.data = self.data.drop(columns=name)
        
    def display(self):
        print(self.data)

    def calculate_mean(self, column_name):
        column_values = [c.values for c in self.columns if c.name == column_name][0]
        return sum(column_values)

    def get_max(self, column_name):
        column_values = [c.values for c in self.columns if c.name == column_name][0]
        return max(column_values)
        

class CSVColumn:
    def __init__(self, name, values):
        self.name = name
        self.values = values


if __name__ == "__main__":
    csv_file = CSVFile('Video_Games_Sales_2016.csv')
    csv_file.display()

    EUA_sales = csv_file.calculate_mean('EU_Sales')
    print(f"O total de vendas nos EUA é: U$ {EUA_sales:.2f}")

    max_grade = csv_file.get_max('Global_Sales')
    print(f"A maior Venda Global é : U$ {max_grade}")
