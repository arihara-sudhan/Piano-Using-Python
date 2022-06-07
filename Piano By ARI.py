import sys
import pygame as ARI
import time

ARI.init()
ARI.mixer.init()


# MUSICS
# ----------------------------------------------------------------------------------------------
def CLINK1():
    Clink1 = ARI.mixer.music.load('Clink1.mp3')
    ARI.mixer.music.play()


def CLINK2():
    Clink1 = ARI.mixer.music.load('Clink2.mp3')
    ARI.mixer.music.play()


def CLINK3():
    Clink1 = ARI.mixer.music.load('Clink3.mp3')
    ARI.mixer.music.play()


def CLINK4():
    Clink1 = ARI.mixer.music.load('Clink4.mp3')
    ARI.mixer.music.play()


def CLINK5():
    Clink1 = ARI.mixer.music.load('Clink5.mp3')
    ARI.mixer.music.play()


def CLINK6():
    Clink1 = ARI.mixer.music.load('Clink6.mp3')
    ARI.mixer.music.play()


def CLINK7():
    Clink1 = ARI.mixer.music.load('Clink7.mp3')
    ARI.mixer.music.play()


# SCREEN
# ----------------------------------------------------------------------------------------------
w, h = 16 * 84, 10 * 70
Bg_ARI = ARI.display.set_mode((w, h), 0, 0)
ARI.display.set_caption("ARI'S PIANO")

# PIANO KEYBOARD
# ----------------------------------------------------------------------------------------------
Piano_KEY = ARI.image.load("Piano_KEY2.jpg")
Piano_KEY = ARI.transform.scale(Piano_KEY, (w, h))
Clicked = ARI.image.load("Clicked.png")
Clicked = ARI.transform.scale(Clicked, (200, h-2))
Sel = ARI.image.load("Sel.png")
Sel = ARI.transform.scale(Sel, (496, 100+70+1))
Bg_ARI.blit(Piano_KEY, (0, 0))
INTRO = ARI.image.load("INTROP.jpg")
INTRO = ARI.transform.scale(INTRO, (w, h))


def BGBLIT():
    Bg_ARI.blit(Piano_KEY, (0, 0))


cx, cy = 0, 50


def CLICKED(cx):
    Bg_ARI.blit(Clicked, (cx, cy))
    ARI.display.update()


sleep = 0.09
sleep1 = 4
Bg_ARI.blit(INTRO, (0, 0))
ARI.display.update()
a = 1
while (a == 1):
    for Eveu in ARI.event.get():
        if Eveu.type == ARI.QUIT:
            a = 0
        elif Eveu.type == ARI.KEYDOWN:
            if Eveu.key == ARI.K_RETURN:
                Bg_ARI.blit(Sel, (120+30+10, 187))
                ARI.display.update()
                time.sleep(2)
                b = 1
                a = 0
                BGBLIT()

            if Eveu.key == ARI.K_ESCAPE:
                Bg_ARI.blit(Sel, (120+30+10, 187+100+20-5))
                ARI.display.update()
                time.sleep(2)
                ARI.display.quit()
                sys.exit()

# EVENT-PIANO
# ----------------------------------------------------------------------------------------------
while (b == 1):
    for EveMu in ARI.event.get():
        if EveMu.type == ARI.QUIT:
            ARI.display.quit()
            sys.exit()
        elif EveMu.type == ARI.KEYDOWN:
            if EveMu.key == ARI.K_z:
                cx = -50
                CLICKED(cx)
                CLINK1()
                time.sleep(sleep)
                BGBLIT()

            if EveMu.key == ARI.K_x:
                cx = 150
                CLICKED(cx)
                CLINK2()
                time.sleep(sleep)
                BGBLIT()

            if EveMu.key == ARI.K_c:
                cx = 150 * 3 - 90
                CLICKED(cx)
                CLINK3()
                time.sleep(sleep)
                BGBLIT()

            if EveMu.key == ARI.K_v:
                cx = 150 * 4 - 40
                CLICKED(cx)
                CLINK4()
                time.sleep(sleep)
                BGBLIT()

            if EveMu.key == ARI.K_b:
                cx = 150 * 5 + 20
                CLICKED(cx)
                CLINK5()
                time.sleep(sleep)
                BGBLIT()

            if EveMu.key == ARI.K_n:
                cx = 150 * 6 + 70
                CLICKED(cx)
                CLINK6()
                time.sleep(sleep)
                BGBLIT()

            if EveMu.key == ARI.K_m:
                cx = 150 * 7 + 50 + 80
                CLICKED(cx)
                CLINK7()
                time.sleep(sleep)
                BGBLIT()

    ARI.display.update()
ARI.quit()

def SOMEMUSIC():
    while (a == 1):
        for Eveu in ARI.event.get():
            if Eveu.type == ARI.QUIT:
                a = 0
            elif Eveu.type == ARI.KEYDOWN:
                if Eveu.key == ARI.K_RETURN:
                    Bg_ARI.blit(Sel, (120+30+10, 187))
                    ARI.display.update()
                    time.sleep(2)
                    b = 1
                    a = 0
                    BGBLIT()

                if Eveu.key == ARI.K_ESCAPE:
                    Bg_ARI.blit(Sel, (120+30+10, 187+100+20-5))
                    ARI.display.update()
                    time.sleep(2)
                    ARI.display.quit()
                    sys.exit()

    # EVENT-PIANO
    # ----------------------------------------------------------------------------------------------
    while (b == 1):
        for EveMu in ARI.event.get():
            if EveMu.type == ARI.QUIT:
                ARI.display.quit()
                sys.exit()
            elif EveMu.type == ARI.KEYDOWN:
                if EveMu.key == ARI.K_z:
                    cx = -50
                    CLICKED(cx)
                    CLINK1()
                    time.sleep(sleep)
                    BGBLIT()

                if EveMu.key == ARI.K_x:
                    cx = 150
                    CLICKED(cx)
                    CLINK2()
                    time.sleep(sleep)
                    BGBLIT()

                if EveMu.key == ARI.K_c:
                    cx = 150 * 3 - 90
                    CLICKED(cx)
                    CLINK3()
                    time.sleep(sleep)
                    BGBLIT()

                if EveMu.key == ARI.K_v:
                    cx = 150 * 4 - 40
                    CLICKED(cx)
                    CLINK4()
                    time.sleep(sleep)
                    BGBLIT()

                if EveMu.key == ARI.K_b:
                    cx = 150 * 5 + 20
                    CLICKED(cx)
                    CLINK5()
                    time.sleep(sleep)
                    BGBLIT()

                if EveMu.key == ARI.K_n:
                    cx = 150 * 6 + 70
                    CLICKED(cx)
                    CLINK6()
                    time.sleep(sleep)
                    BGBLIT()

                if EveMu.key == ARI.K_m:
                    cx = 150 * 7 + 50 + 80
                    CLICKED(cx)
                    CLINK7()
                    time.sleep(sleep)
                    BGBLIT()

        ARI.display.update()

def SOMEMUSIC2():
    while (a == 1):
        for Eveu in ARI.event.get():
            if Eveu.type == ARI.QUIT:
                a = 0
            elif Eveu.type == ARI.KEYDOWN:
                if Eveu.key == ARI.K_RETURN:
                    Bg_ARI.blit(Sel, (120+30+10, 187))
                    ARI.display.update()
                    time.sleep(2)
                    b = 1
                    a = 0
                    BGBLIT()

                if Eveu.key == ARI.K_ESCAPE:
                    Bg_ARI.blit(Sel, (120+30+10, 187+100+20-5))
                    ARI.display.update()
                    time.sleep(2)
                    ARI.display.quit()
                    sys.exit()

    # EVENT-PIANO
    # ----------------------------------------------------------------------------------------------
    while (b == 1):
        for EveMu in ARI.event.get():
            if EveMu.type == ARI.QUIT:
                ARI.display.quit()
                sys.exit()
            elif EveMu.type == ARI.KEYDOWN:
                if EveMu.key == ARI.K_z:
                    cx = -50
                    CLICKED(cx)
                    CLINK1()
                    time.sleep(sleep)
                    BGBLIT()

                if EveMu.key == ARI.K_x:
                    cx = 150
                    CLICKED(cx)
                    CLINK2()
                    time.sleep(sleep)
                    BGBLIT()

                if EveMu.key == ARI.K_c:
                    cx = 150 * 3 - 90
                    CLICKED(cx)
                    CLINK3()
                    time.sleep(sleep)
                    BGBLIT()

                if EveMu.key == ARI.K_v:
                    cx = 150 * 4 - 40
                    CLICKED(cx)
                    CLINK4()
                    time.sleep(sleep)
                    BGBLIT()

                if EveMu.key == ARI.K_b:
                    cx = 150 * 5 + 20
                    CLICKED(cx)
                    CLINK5()
                    time.sleep(sleep)
                    BGBLIT()

                if EveMu.key == ARI.K_n:
                    cx = 150 * 6 + 70
                    CLICKED(cx)
                    CLINK6()
                    time.sleep(sleep)
                    BGBLIT()

                if EveMu.key == ARI.K_m:
                    cx = 150 * 7 + 50 + 80
                    CLICKED(cx)
                    CLINK7()
                    time.sleep(sleep)
                    BGBLIT()

        ARI.display.update()