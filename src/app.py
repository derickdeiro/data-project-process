from frontend import ExcelValidatorUI

def main():
    ui = ExcelValidatorUI()
    ui.display_header()
    ui.upload_file()

if __name__ == '__main__':
    main()