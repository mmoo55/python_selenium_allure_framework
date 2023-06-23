# python_selenium_allure_framework

1. Instalacion de paquetes:
	- selenium
	- edgedriver-autoinstaller
	- chromedriver-autoinstaller
	- geckodriver-autoinstaller
	- python-dotenv
	- openpyxl
	- ddt

2. Para allure:
	- selenium
	- pytest
	- allure-pytest

	- Comando para hacer correr:
		pytest -v -s --alluredir="allure_reports" .\test_suite\test_login.py
	
	- Comando para mostrar el reporte:
		allure serve allure_reports/

3. Para correr con pytest:
	- pytest -v -s .\test_suite\test_login.py