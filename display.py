import sys
import html

from PyQt5.QtGui import QFont, QFontMetrics, QGuiApplication
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit

import barcode_product_scanner as base


BASE_SCREEN_WIDTH = 1366
BASE_SCREEN_HEIGHT = 768


def compute_ui_scale():
    screen = QGuiApplication.primaryScreen()
    if screen is None:
        return 1.0
    geometry = screen.availableGeometry()
    width_scale = geometry.width() / BASE_SCREEN_WIDTH
    height_scale = geometry.height() / BASE_SCREEN_HEIGHT
    return max(1.0, min(width_scale, height_scale, 1.35))


UI_SCALE = compute_ui_scale()

base.BASE_FONT_SIZE = round(16 * UI_SCALE)
base.HEADER_FONT_SIZE = round(18 * UI_SCALE)
base.TABLE_FONT_SIZE = round(18 * UI_SCALE)
base.STATUS_FONT_SIZE = round(14 * UI_SCALE)
base.SMALL_FONT_SIZE = round(12 * UI_SCALE)
base.DESCRIPTION_FONT_SIZE = round(18 * UI_SCALE)
base.ROW_HEIGHT = round(110 * UI_SCALE)
DESCRIPTION_WRAP_WIDTH = 28
PRINT_PAGE_WIDTH_PT = 612
PRINT_PAGE_HEIGHT_PT = 792
PRINT_MARGIN_MM = 6.35
PRINT_MARGIN_PT = 18


class DisplayApp(base.BarcodeProductScannerApp):
    def __init__(self):
        super().__init__()
        self.configure_variant()

    def configure_variant(self):
        self.setWindowTitle("Display")
        self.table.setColumnHidden(self.PHOTO_COLUMN, True)
        self.table.setColumnHidden(self.PRICE_COLUMN, True)
        self.apply_adaptive_layout()

    def apply_adaptive_layout(self):
        screen = QGuiApplication.primaryScreen()
        if screen is not None:
            geometry = screen.availableGeometry()
            width = max(BASE_SCREEN_WIDTH, geometry.width())
            height = max(BASE_SCREEN_HEIGHT, geometry.height())
            self.resize(width, height)

        self.set_description_column_width()
        self.set_compact_column_widths()

    def set_compact_column_widths(self):
        screen = QGuiApplication.primaryScreen()
        available_width = BASE_SCREEN_WIDTH
        if screen is not None:
            available_width = max(BASE_SCREEN_WIDTH, screen.availableGeometry().width())

        scale = available_width / BASE_SCREEN_WIDTH
        widths = {
            self.ITEM_CODE_COLUMN: round(145 * scale),
            self.WH1_QTY_COLUMN: round(72 * scale),
            self.WH2_QTY_COLUMN: round(72 * scale),
            self.WH6_QTY_COLUMN: round(72 * scale),
            self.TOTAL_QTY_COLUMN: round(90 * scale),
            self.REQUEST_QTY_COLUMN: round(155 * scale),
            self.WAREHOUSE_COLUMN: round(110 * scale),
            self.SHOWROOM_COLUMN: round(110 * scale),
            self.DELETE_COLUMN: round(78 * scale),
        }
        for column, width in widths.items():
            self.table.setColumnWidth(column, width)

    def set_description_column_width(self):
        font = QFont(self.table.font())
        font.setPixelSize(base.DESCRIPTION_FONT_SIZE)
        font.setBold(True)
        metrics = QFontMetrics(font)
        text_width = int(metrics.averageCharWidth() * DESCRIPTION_WRAP_WIDTH)
        padding_width = metrics.horizontalAdvance("  ") + 6
        self.table.setColumnWidth(self.DESCRIPTION_COLUMN, text_width + padding_width)

    def make_table_item(
        self,
        text,
        alignment=base.Qt.AlignCenter,
        background=None,
        font_pixel_size=None,
        tooltip=None,
        missing=False,
    ):
        item = super().make_table_item(
            text=text,
            alignment=alignment,
            background=background,
            font_pixel_size=font_pixel_size,
            tooltip=tooltip,
            missing=missing,
        )
        font = QFont(item.font())
        if font_pixel_size is None:
            font.setPixelSize(base.TABLE_FONT_SIZE)
        font.setBold(True)
        item.setFont(font)
        return item

    def create_request_qty_widget(self):
        widget = super().create_request_qty_widget()
        for label in widget.findChildren(QLabel):
            label.setStyleSheet(
                f"font-size: {base.SMALL_FONT_SIZE}px; font-weight: bold; color: #555;"
            )
        for line_edit in widget.findChildren(QLineEdit):
            line_edit.setStyleSheet(
                f"font-size: {base.SMALL_FONT_SIZE}px; font-weight: bold; padding: 1px 4px; min-height: 18px;"
            )
        return widget

    def get_request_qty_print_text(self, row_idx):
        request_widget = self.table.cellWidget(row_idx, self.REQUEST_QTY_COLUMN)
        qty_inputs = getattr(request_widget, "qty_inputs", {})
        parts = []
        label_map = {
            "case": "Case",
            "inner": "Inner",
            "unit": "PC",
        }

        for key in ("case", "inner", "unit"):
            _, line_edit = qty_inputs.get(key, ("", None))
            if line_edit is None:
                continue
            value = line_edit.text().strip()
            if value and value != "0":
                parts.append(f"{value} {label_map[key]}")

        return "  ".join(parts)

    def get_warehouse_group_key(self, warehouse_text):
        normalized = (warehouse_text or "").strip()
        if not normalized:
            return "#"
        return normalized[0].upper()

    def build_print_row_data(self, row_idx):
        warehouse_text = self.get_item_text(row_idx, self.WAREHOUSE_COLUMN)
        item_code = self.get_item_text(row_idx, self.ITEM_CODE_COLUMN)
        return {
            "group_key": self.get_warehouse_group_key(warehouse_text),
            "warehouse_text": warehouse_text,
            "item_code": item_code,
            "html": (
                "<tr>"
                + self.build_print_cell_html(
                    item_code,
                    "",
                    extra_class="item-code-cell",
                )
                + self.build_print_cell_html(
                    self.get_item_text(row_idx, self.DESCRIPTION_COLUMN),
                    align_left=True,
                    wrap_text=True,
                    extra_class="desc-cell",
                )
                + self.build_print_cell_html(
                    self.get_item_text(row_idx, self.WH1_QTY_COLUMN),
                    "",
                )
                + self.build_print_cell_html(
                    self.get_request_qty_print_text(row_idx),
                    "",
                )
                + self.build_print_cell_html(
                    warehouse_text,
                    self.get_print_cell_class(row_idx, self.WAREHOUSE_COLUMN, False),
                )
                + self.build_print_cell_html(
                    self.get_item_text(row_idx, self.SHOWROOM_COLUMN),
                    self.get_print_cell_class(row_idx, self.SHOWROOM_COLUMN, False),
                )
                + "</tr>"
            ),
        }

    def print_table(self):
        if self.table.rowCount() == 0:
            base.QMessageBox.information(self, "Info", "There is nothing to print.")
            return

        sales_name = self.prompt_sales_name("Print")
        if sales_name is None:
            return

        current_dt = self.get_current_us_eastern_time()
        sales_meta_html = (
            f"{'&nbsp;' * 40}"
            f"{html.escape(sales_name.upper())}"
            f"&nbsp;&nbsp;&nbsp;"
            f"{html.escape(self.format_sales_time(current_dt))}"
        )

        printer = base.QPrinter(base.QPrinter.HighResolution)
        printer.setPaperSize(base.QPrinter.Letter)
        printer.setOrientation(base.QPrinter.Portrait)
        printer.setFullPage(False)
        printer.setPageMargins(
            PRINT_MARGIN_MM,
            PRINT_MARGIN_MM,
            PRINT_MARGIN_MM,
            PRINT_MARGIN_MM,
            base.QPrinter.Millimeter,
        )
        dialog = base.QPrintDialog(printer, self)
        if dialog.exec_() != base.QPrintDialog.Accepted:
            return

        printer.setPaperSize(base.QPrinter.Letter)
        printer.setOrientation(base.QPrinter.Portrait)
        printer.setFullPage(False)
        printer.setPageMargins(
            PRINT_MARGIN_MM,
            PRINT_MARGIN_MM,
            PRINT_MARGIN_MM,
            PRINT_MARGIN_MM,
            base.QPrinter.Millimeter,
        )

        saved_file_path = self.save_table_to_excel(
            sales_name=sales_name,
            current_dt=current_dt,
            update_status=False,
        )
        if saved_file_path is None:
            return

        headers = [
            "Item Code",
            "Description",
            "W1",
            "Request Qty",
            "Warehouse",
            "Showroom",
        ]

        header_html = "".join(f"<th>{html.escape(title)}</th>" for title in headers)
        print_rows = [self.build_print_row_data(row_idx) for row_idx in range(self.table.rowCount())]
        print_rows.sort(
            key=lambda row: (
                not row["warehouse_text"],
                row["warehouse_text"],
                row["item_code"],
            )
        )

        body_html_rows = [row["html"] for row in print_rows]

        document = base.QTextDocument()
        document.setDocumentMargin(0)
        document.setPageSize(
            base.QSizeF(
                PRINT_PAGE_WIDTH_PT - (PRINT_MARGIN_PT * 2),
                PRINT_PAGE_HEIGHT_PT - (PRINT_MARGIN_PT * 2),
            )
        )
        document.setHtml(
            f"""
            <html>
                <head>
                    <style>
                        @page {{
                            size: Letter portrait;
                            margin: 0;
                        }}
                        body {{
                            font-family: Arial, sans-serif;
                            font-size: 8.5pt;
                            margin: 0;
                        }}
                        .page {{
                            width: {PRINT_PAGE_WIDTH_PT - (PRINT_MARGIN_PT * 2)}pt;
                            margin: 0;
                        }}
                        .header-line {{
                            font-size: 11pt;
                            font-weight: bold;
                            margin-bottom: 6px;
                            white-space: nowrap;
                        }}
                        table.data-table {{
                            width: 100%;
                            border-collapse: collapse;
                            table-layout: auto;
                        }}
                        col.code {{ width: 1%; }}
                        col.desc {{ width: 45%; }}
                        col.qty {{ width: 8%; }}
                        col.req {{ width: 17%; }}
                        col.wh {{ width: 12%; }}
                        col.show {{ width: 9%; }}
                        th, td {{
                            border: 1px solid #666;
                            padding: 4px 5px;
                            white-space: nowrap;
                            overflow: hidden;
                        }}
                        th {{
                            background-color: #f2f2f2;
                            text-align: center;
                            font-weight: bold;
                        }}
                        td.center {{
                            text-align: center;
                        }}
                        td.left {{
                            text-align: left;
                        }}
                        td.wrap {{
                            white-space: normal;
                            word-break: break-word;
                            line-height: 1.15;
                        }}
                        td.desc-cell {{
                            font-size: 6.5pt;
                        }}
                        td.item-code-cell {{
                            font-weight: bold;
                            font-size: 9.5pt;
                            white-space: pre;
                            padding-left: 0;
                            padding-right: 0;
                        }}
                        td.warning {{
                            background-color: #ff9e9e;
                        }}
                        td.missing {{
                            background-color: #e8e8e8;
                            color: #666;
                        }}
                    </style>
                </head>
                <body>
                    <div class="page">
                        <div class="header-line">Display{sales_meta_html}</div>
                        <table class="data-table">
                            <colgroup>
                                <col class="code">
                                <col class="desc">
                                <col class="qty">
                                <col class="req">
                                <col class="wh">
                                <col class="show">
                            </colgroup>
                            <thead>
                                <tr>{header_html}</tr>
                            </thead>
                            <tbody>
                                {''.join(body_html_rows)}
                            </tbody>
                        </table>
                    </div>
                </body>
            </html>
            """
        )
        document.print_(printer)
        self.status_label.setText(f"Printed and saved: {saved_file_path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = DisplayApp()
    window.show()
    sys.exit(app.exec_())
