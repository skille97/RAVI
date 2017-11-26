cd RAVI

python3 manage.py makemigrations
python3 manage.py makemigrations board
python3 manage.py migrate


echo "Kør 'python3 manage.py createsuperuser' hvis du vil lave en admin konto til 'localhost:8000/admin'"
echo "Kør 'python3 manage.py runserver' for at starte serveren"
echo "Husk at debugmode er slået til og at du skal køre denne fil hver gang du ændrer på modellerne i models.py"
