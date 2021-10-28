# (c) 2021 Itai Shek
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


def unsolvable_popup(self, btn):
    content = BoxLayout(orientation="vertical", padding=10)
    popup_label = Label(text='The board in not solvable.\n\nCheck your input and try again.',
                        size_hint=(1, 3),
                        valign='top'
                        )
    popup_label.bind(size=lambda s, w: s.setter('text_size')(s, w))
    close_popup = Button(text="close")

    content.add_widget(popup_label)
    content.add_widget(close_popup)

    popup = Popup(title='No solutions',
                  content=content,
                  size_hint=(0.4, 0.4),
                  auto_dismiss=False
                  )
    popup.open()

    close_popup.bind(on_press=popup.dismiss)
    btn.disabled = False


def about_popup(self, *args):
    content = BoxLayout(orientation="vertical", padding=10)
    popup_label = Label(text=f'Sudoku solver.\nVersion: {self.__version__}\n\nThis sudoku solver uses the backtracking algorithm. As long  as the puzzle is valid a solution is guaranteed.',
                        size_hint=(1, 4),
                        valign='top'
                        )
    popup_label.bind(size=lambda s, w: s.setter('text_size')(s, w))
    close_popup = Button(text="close")

    content.add_widget(popup_label)
    content.add_widget(close_popup)

    popup = Popup(title='About',
                  content=content,
                  size_hint=(0.4, 0.6),
                  auto_dismiss=False
                  )
    popup.open()

    close_popup.bind(on_press=popup.dismiss)
