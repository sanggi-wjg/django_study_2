from typing import List

from sample.service.excel.sample_read_excel_abs import ReadExcelSampleAbs
from sample.service.excel.vo.sample_vo import DataSampleVO


class ReadExcelSample(ReadExcelSampleAbs):
    _skip_sheet_index = [1]
    _min_row = 2

    def _read_sheet_contents(self) -> List[DataSampleVO]:
        result = []
        for sheet_no, sheet_name in enumerate(self._get_sheet_names()):
            rows = self._workbook[sheet_name].iter_rows(min_row = self._min_row)

            for row in rows:
                result.append(self._read_rows(row))

        return result

    def _read_rows(self, row) -> DataSampleVO:
        index, rack_code, product_code, register_date = '', '', '', ''

        for cell in row:
            # print(cell.column_letter, cell.col_idx, cell.value)
            if cell.column_letter == 'A':
                index = cell.value
            if cell.column_letter == 'B':
                rack_code = cell.value
            if cell.column_letter == 'F':
                register_date = cell.value
            if cell.column_letter == 'I':
                product_code = cell.value

        vo = DataSampleVO(index, rack_code, product_code, register_date)
        vo.validate()
        return vo
