# Pandas

* Create Pandas DataFrame, [link](https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/)

  ```python
  # Method 1: Creating Pandas DataFrame from lists of list
  data = [['tom', 10], ['nick', 15], ['juli', 14]]
  df = pd.DataFrame(data, columns = ['Name', 'Age'])
  
  # Method 2: Creating DataFrame form dict of NArray / lists
  data = {'Name' : ['Tom', 'nick', 'krish', 'jack'],
          'Age' : [20, 21, 19, 18]}
  df = pd.DataFrame(data)
  
  # Method 3: Create an indexed DataFrame using arrays
  data = {'Name' : ['Tom', 'Jack', 'nick', 'juli'],
          'marks' : [99, 98, 95, 90]}
  df = pd.DataFrame(data, index = ['rank1', 'rank2', 'rank3', 'rank4'])
  ```

  

##### Reading & Writing Files

* Read xlsx file, [link](https://stackoverflow.com/questions/16888888/how-to-read-a-xlsx-file-using-the-pandas-library-in-ipython)

  ```python
  df_samples = pd.read_excel(r'filename.xlsx', engine = 'openpyxl')
  ```

* Read Excel with merged cells, [link](https://stackoverflow.com/questions/22937650/pandas-reading-excel-with-merged-cells)

  ```python
  df.index = pd.Series(df.index).fillna(method = 'ffill')
  ```

* Read Excel background color, [link](https://stackoverflow.com/questions/47857112/get-excel-cell-background-color-in-pandas-read-excel)

  ```python
  from xlrd import open_workbook
  wb = open_workbook('wb.xls', formatting_info = True)
  sheet = wb.sheet_by_name("mysheet")
  
  # create empy colormask matrix
  bgcol = np.zeros([sheet.nrows, sheet.ncols])
  
  # cycle through all cells to get colors
  for row in range(sheet.nrows):
    for column in range(sheet.ncols):
      cell = sheet.cell(row, column)  
      fmt = wb.xf_list[cell.xf_index]
      bgcol[row,column] = fmt.background.background_colour_index
  
  # return pandas mask of colors
  colormask = pd.DataFrame(bgcol)
  ```



**Checklist**

- [ ] locating using index
- [ ] apply, map, replace