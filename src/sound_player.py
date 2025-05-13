import pygame

class SoundPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {
            "background": "music/music_background.mp3",
            "wait": "music/music_wait.mp3",
            "fail": "music/sound_fail.wav",
            "hit": "music/sound_hit.wav",
            "led_special": "music/sound_led_2_special.wav",
            "special_hit": "music/sound_special_hit_3pt.wav"
        }

    def play_sound(self, sound_name):
        if sound_name in self.sounds:
            pygame.mixer.music.load(self.sounds[sound_name])
            pygame.mixer.music.play()
        else:
            print(f"Sound '{sound_name}' not found.")

    def stop_sound(self):
        pygame.mixer.music.stop()

    def play_effect(self, effect_name):
        if effect_name in self.sounds:
            sound = pygame.mixer.Sound(self.sounds[effect_name])
            sound.play()
        else:
            print(f"Effect '{effect_name}' not found.")