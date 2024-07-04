import openpyxl
class Excel:
    @staticmethod
    def get_data(filepath,sheet_name,row,col):
      try:
           wb= openpyxl.load_workbook(filepath)
           sheet=wb[sheet_name]
           value=sheet.cell(row,col).value
      except:
           value=""

      return value
