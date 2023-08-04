import os
import pygame
import flet as ft

class MusicPlayer:
    def __init__(self):
        self.music_directory = None
        self.photo_directory = None
        self.playlist = []
        self.photolist = []
        self.current_song = 0
        pygame.mixer.init()
        
    def load_music(self):
        self.music_directory = "Songs"
        self.photo_directory = "Images"
        if self.music_directory:
            self.playlist = []
            for file in os.listdir(self.music_directory):
                if file.endswith(".mp3"):
                    self.playlist.append(os.path.join(self.music_directory, file))
        if self.photo_directory:
            self.photolist = []
            for pic in os.listdir(self.photo_directory):
                if pic.endswith(".png"):
                    self.photolist.append(os.path.join(self.photo_directory, pic))

    def play(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_song])
            pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()

    def next_song(self):
        self.current_song = (self.current_song + 1) % len(self.playlist)
        self.play()

    def previous_song(self):
        self.current_song = (self.current_song - 1) % len(self.playlist)
        self.play()

def main(page: ft.Page):
    page.title = "Music App"
    page.window_height = 800
    page.window_width = 600
    page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    music_player = MusicPlayer()
    music_player.load_music()

    head = ft.Text("Music App", size=25, text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.W_900)
    img = ft.Image(
        width=400,
        height=200,
        fit=ft.ImageFit.CONTAIN
    )
    
    img.src = music_player.photolist[music_player.current_song]

    def prev_sg(e):
        music_player.previous_song()
        img.src = music_player.photolist[music_player.current_song]
        page.update()

    def pause_sg(e):
        music_player.pause()

    def play_sg(e):
        music_player.play()

    def stop_sg(e):
        music_player.stop()

    def next_sg(e):
        music_player.next_song()
        img.src = music_player.photolist[music_player.current_song]
        page.update()


    iconrow = ft.Row([
        ft.IconButton(icon=ft.icons.SKIP_PREVIOUS_ROUNDED, icon_color="pink400", icon_size=40, tooltip="Previous", on_click=prev_sg),
        ft.IconButton(icon=ft.icons.PAUSE_CIRCLE_ROUNDED, icon_color="pink400", icon_size=50, tooltip="Pause", on_click=pause_sg),
        ft.IconButton(icon=ft.icons.PLAY_CIRCLE_ROUNDED, icon_color="pink400", icon_size=60, tooltip="Play", on_click=play_sg),
        ft.IconButton(icon=ft.icons.STOP_CIRCLE_ROUNDED, icon_color="pink400", icon_size=50, tooltip="Stop", on_click=stop_sg),
        ft.IconButton(icon=ft.icons.SKIP_NEXT_ROUNDED, icon_color="pink400", icon_size=40, tooltip="Next", on_click=next_sg),
    ],alignment=ft.MainAxisAlignment.CENTER)

    col = ft.Column([
        ft.Container(
            content=head,
            alignment=ft.alignment.bottom_center,
        ),
        ft.Container(
            content=img,
            alignment=ft.alignment.bottom_right,
        ),
        ft.Container(
            content=iconrow,
            padding=5,
            alignment=ft.alignment.center,
        )
    ],
    width=400)

    cont = ft.Container(
        content=col,
        padding=20,
        border_radius=10,
        border=ft.border.all(2, '#000000'),
    )

    page.add(
        cont,
    )

ft.app(target=main)
