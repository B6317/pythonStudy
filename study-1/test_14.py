# coding=utf-8
# create by toonew at 2018/2/22
import xlwt
import json

str1 = repr(
    {
        "1": ["张三", 150, 120, 100],
        "2": ["李四", 90, 99, 95],
        "3": ["王五", 60, 66, 68]
    }
)
jo = json.loads(str1)

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
                     num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding='utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('My Worksheet')

# 写入excel
# 参数对应 行, 列, 值
worksheet.write(1, 0, label='this is test')

# 保存
workbook.save('./test/Excel_test.xls')
