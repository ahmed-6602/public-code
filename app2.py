from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class User:
    def _init_(self, username, password):
        self.username = username
        self.password = password

class Teacher(User):
    def _init_(self, username, password):
        super()._init_(username, password)
        self.notes = []
        self.attendance = {}

    def upload_notes(self, notes):
        self.notes.append(notes)

    def mark_attendance(self, student):
        self.attendance[student.username] = True

class Student(User):
    def _init_(self, username, password):
        super()._init_(username, password)
        self.questions_paper = []

    def get_questions_paper(self, questions_paper):
        self.questions_paper.append(questions_paper)

class MyApp(App):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        self.users = []

    def build(self):
        layout = BoxLayout(orientation='vertical')

        teacher_button = Button(text='Teacher', on_press=self.teacher_login)
        student_button = Button(text='Student', on_press=self.student_login)

        layout.add_widget(teacher_button)
        layout.add_widget(student_button)

        return layout

    def teacher_login(self, instance):
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Teacher Login')
        layout.add_widget(label)

        username_label = Label(text='Username:')
        username_input = TextInput()
        password_label = Label(text='Password:')
        password_input = TextInput(password=True)

        login_button = Button(text='Login', on_press=self.teacher_logged_in)

        layout.add_widget(username_label)
        layout.add_widget(username_input)
        layout.add_widget(password_label)
        layout.add_widget(password_input)
        layout.add_widget(login_button)

        self.root.clear_widgets()
        self.root.add_widget(layout)

    def teacher_logged_in(self, instance):
        # Authenticate teacher and proceed with teacher interface
        pass

    def student_login(self, instance):
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Student Login')
        layout.add_widget(label)

        username_label = Label(text='Username:')
        username_input = TextInput()
        password_label = Label(text='Password:')
        password_input = TextInput(password=True)

        login_button = Button(text='Login', on_press=self.student_logged_in)

        layout.add_widget(username_label)
        layout.add_widget(username_input)
        layout.add_widget(password_label)
        layout.add_widget(password_input)
        layout.add_widget(login_button)

        self.root.clear_widgets()
        self.root.add_widget(layout)

    def student_logged_in(self, instance):
        # Authenticate student and proceed with student interface
        pass

if __name__ == '_main_':
    MyApp().run()



print("Executed Successfully")
