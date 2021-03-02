### Address book on DRF and Vue.js
Address book including:  
Fields:
- Name
- Surname
- Address
- Telephone

Features:
- Add person
- Delete person
- Change person
- Filter by name, surname and telephone

All people require name, surname and telephone

To change person click on button "Edit"

To delete person click on button "Delete"

URL should be started from http

### Install 
```bash
. .\.venv\Scripts\activate
pip install -r requirements.txt
python backend/manage.py migrate
cd ./frontend
npm i
npm run serve
python backend/manage.py runserver
```
link:http://localhost:8080/

To run tests go to ./backend and run
```bash
python manage.py test
```