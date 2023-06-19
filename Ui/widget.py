import sys
import requests
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from ui_form import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowTitle("BackBD - Sistema de gerenciamento")

        # Users:
        self.ui.pbcuser.clicked.connect(self.UserCallAPIPost)
        self.ui.pbsuser.clicked.connect(self.UserCallAPI)
        self.ui.pbauser.clicked.connect(self.UserCallAPIPut)
        self.ui.pbeuser.clicked.connect(self.UserCallAPIDelete)

        # Games
        self.ui.pbcgame.clicked.connect(self.GameCallAPIPost)
        self.ui.pbsgame.clicked.connect(self.GameCallAPI)
        self.ui.pbagame.clicked.connect(self.GameCallAPIPut)
        self.ui.pbegame.clicked.connect(self.GameCallAPIDelete)

        #UHG
        self.ui.pbcuhg.clicked.connect(self.UHGCallAPIPost)
        self.ui.pbsuhg.clicked.connect(self.UHGCallAPI)
        self.ui.pbauhg.clicked.connect(self.UHGCallAPIPut)
        self.ui.pbeuhg.clicked.connect(self.UHGCallAPIDelete)


        # Toggle
        self.ui.pushButton.clicked.connect(self.leftMenu)

        # Pages
        self.ui.pushButton_2.clicked.connect(lambda: self.showPage(self.ui.pg_user))
        self.ui.pushButton_3.clicked.connect(lambda: self.showPage(self.ui.pg_game))
        self.ui.pushButton_4.clicked.connect(lambda: self.showPage(self.ui.pg_uhg))
        self.showPage(self.ui.pg_user)

        # Animation
        self.animation = None

    def leftMenu(self):
        width = self.ui.left_container.width()

        if width == 9:
            newWidth = 200
        else:
            newWidth = 9

        self.animation = QPropertyAnimation(self.ui.left_container, b"maximumWidth")
        self.animation.setDuration(100)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def showPage(self, page):
        self.ui.pg_user.setVisible(page == self.ui.pg_user)
        self.ui.pg_game.setVisible(page == self.ui.pg_game)
        self.ui.pg_uhg.setVisible(page == self.ui.pg_uhg)

    def UserCallAPI(self):
        userID = self.ui.userid.text()
        response = requests.get(f"http://localhost:5000/api/users/{userID}")
        data = response.json()
        self.ui.username.setText(data["name"])
        self.ui.usergender.setText(data["gender"])
        self.ui.userage.setText(str(data["age"]))

    def UserCallAPIPost(self):
        name = self.ui.username.text()
        gender = self.ui.usergender.text()
        age = self.ui.userage.text()
        data = {
            "name": name,
            "gender": gender,
            "age": age
        }
        response = requests.post("http://localhost:5000/api/users", json=data)
        self.ui.username.setText("")
        self.ui.usergender.setText("")
        self.ui.userage.setText("")
        print(response.json())

    def UserCallAPIPut(self):
        id = self.ui.userid.text()
        name = self.ui.username.text()
        gender = self.ui.usergender.text()
        age = self.ui.userage.text()
        data = {
            "name": name,
            "gender": gender,
            "age": age
        }
        response = requests.put(f"http://localhost:5000/api/users/{id}", json=data)
        self.ui.userid.setText("")
        self.ui.username.setText("")
        self.ui.usergender.setText("")
        self.ui.userage.setText("")
        print(response.json())

    def UserCallAPIDelete(self):
        userID = self.ui.userid.text()
        response = requests.delete(f"http://localhost:5000/api/users/{userID}")
        print(response.json())

    def GameCallAPI(self):
        gameID = self.ui.gameid.text()
        response = requests.get(f"http://localhost:5000/api/games/{gameID}")
        data = response.json()
        self.ui.gamename.setText(data["name"])
        self.ui.platgame.setText(data["platform"])
        self.ui.gamegender.setText(data["genre"])
        self.ui.gamedura.setText(str(data["duration"]))

    def GameCallAPIPost(self):
        name = self.ui.gamename.text()
        platform = self.ui.platgame.text()
        genre = self.ui.gamegender.text()
        duration = self.ui.gamedura.text()
        data = {
            "name": name,
            "platform": platform,
            "genre": genre,
            "duration": duration
        }
        response = requests.post("http://localhost:5000/api/games", json=data)
        self.ui.gamename.setText("")
        self.ui.platgame.setText("")
        self.ui.gamegender.setText("")
        self.ui.gamedura.setText("")
        print(response.json())

    def GameCallAPIPut(self):
        id = self.ui.gameid.text()
        name = self.ui.gamename.text()
        platform = self.ui.platgame.text()
        genre = self.ui.gamegenre.text()
        duration = self.ui.gamedura.text()
        data = {
            "name": name,
            "platform": platform,
            "genre": genre,
            "duration": duration
        }
        response = requests.put(f"http://localhost:5000/api/games/{id}", json=data)
        self.ui.gameid.setText("")
        self.ui.gamename.setText("")
        self.ui.platgame.setText("")
        self.ui.gamegenre.setText("")
        self.ui.gamedura.setText("")
        print(response.json())

    def GameCallAPIDelete(self):
        gameID = self.ui.gameid.text()
        response = requests.delete(f"http://localhost:5000/api/games/{gameID}")
        print(response.json())
    
    def UHGCallAPI(self):
        uhgID = self.ui.uhgid.text()
        response = requests.get(f"http://localhost:5000/api/Uhg/{uhgID}")
        data = response.json()
        self.ui.uhguserid.setText(str(data["user_id"]))
        self.ui.uhggameid.setText(str(data["game_id"]))
        self.ui.uhgrate.setText(str(data["rate"]))
        self.ui.uhgreview.setText((data["review"]))

    def UHGCallAPIPost(self):
        userid = self.ui.uhguserid.text()
        gameid = self.ui.uhggameid.text()
        rate = self.ui.uhgrate.text()
        review = self.ui.uhgreview.text()
        data = {
            "user_id": userid,
            "game_id": gameid,
            "rate": rate,
            "review": review
        }
        response = requests.post("http://localhost:5000/api/Uhg", json=data)
        self.ui.uhguserid.setText("")
        self.ui.uhggameid.setText("")
        self.ui.uhgrate.setText("")
        self.ui.uhgreview.setText("")
        print(response.json())
    
    def UHGCallAPIPut(self):
        id = self.ui.uhgid.text()
        userid = self.ui.uhguserid.text()
        gameid = self.ui.uhggameid.text()
        rate = self.ui.uhgrate.text()
        review = self.ui.uhgreview.text()
        data = {
            "user_id": userid,
            "game_id": gameid,
            "rate": rate,
            "review": review
        }
        response = requests.put(f"http://localhost:5000/api/Uhg/{id}", json=data)
        self.ui.uhgid.setText("")
        self.ui.uhguserid.setText("")
        self.ui.uhggameid.setText("")
        self.ui.uhgrate.setText("")
        self.ui.uhgreview.setText("")
        print(response.json())
    def UHGCallAPIDelete(self):
    
        uhgID = self.ui.uhgid.text()
        response = requests.delete(f"http://localhost:5000/api/Uhg/{uhgID}")
        print(response.json())
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.ui.pushButton.setText("==")
    widget.ui.label.setText("BackDB")
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())
