#Создай собственный Шутер!
from random import randint 
from pygame import *

def game():


        

    class GameSprite(sprite.Sprite):
        def __init__(self, player_image,  player_x, player_y, player_speed, w, h):
            super().__init__()
            self.image = transform.scale(image.load(player_image), (w, h))
            self.speed = player_speed
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y
        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))

        
    class Player(GameSprite):
        def update(self):
            keys = key.get_pressed()
            if keys[K_LEFT] and self.rect.x > 5:
                self.rect.x -= self.speed
            if keys[K_RIGHT] and self.rect.x <  620:
                self.rect.x += self.speed
        def fire():
            pass
        def vistrel(self):
            puly = Puly("bullet.png", self.rect.x, self.rect.y, 10, 15,20)
            pulys.add(puly)
    global miss        
    miss = 0        
    class Enemy(GameSprite):
        def update(self):
            if self.rect.y < 650:
                self.rect.y += self.speed



                
            global miss
            

            if self.rect.y >= 650:
                miss += 1
                self.rect.x = randint(80, 1120)
                self.rect.y = randint(-100, -50)
    monsters = sprite.Group()
    class Puly(GameSprite):
        def update(self):
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.kill()
    pulys = sprite.Group()

    player = Player('pngwing.com (1).png',400,420, 7, 75, 75)
    for i in range(5):

        vrag1 = Enemy('ufo.png', randint(0, 635),-65,randint(1,5),80,80)
        monsters.add(vrag1)
    window = display.set_mode((700, 500))
    display.set_caption("Shooter")
    background = transform.scale(image.load("galaxy.jpg"), (700, 500))


    clock = time.Clock()
    FPS = 60

    mixer.init()
    mixer.music.load('space.ogg')
    mixer.music.play(-1)


    kick = mixer.Sound('fire.ogg')



    with open("reiting.txt", "r") as file:
        main_records = file.read()





    font.init()
    score = 0
    finish = False
    run = True
    while run:
        miss_text = font.SysFont("Arial", 35).render("Вы пропустили "+str(miss), True, (255, 255, 255))
        kill_text = font.SysFont("Arial", 35).render("Вы уничтжили "+str(score), True, (255, 255, 255))
        

        for e in event.get():
            if e.type == QUIT:
                run = False
            elif e.type == KEYDOWN:
                if e.key == K_SPACE:
                    player.vistrel()
        if not finish:
            window.blit(background,(0, 0))

            window.blit(miss_text, (10, 10))

            window.blit(kill_text, (10, 30))

            player.reset()
            player.update()
            for i in monsters:
                i.reset()
                i.update()
            for i in pulys:
                i.reset()
                i.update()
            
            kill = sprite.groupcollide(pulys, monsters, True, True)
            for i in kill:
                score += 1
                vrag1 = Enemy('ufo.png', randint(0, 635),-65,randint(1,5),80,80)
                monsters.add(vrag1)
            if miss >= 5:
                finish = True
                best = ''
                with open("reiting.txt", "w") as file:
                    if score > int(main_records):
                        file.write(str(score))
                        best = "вы побили рекорд"
                    else:
                        file.write(str(main_records))
                result = f'Вы уничтожили : {str(score)} {best}'


                
                        


                bed = font.SysFont('Arial', 35).render(result, True, (255, 255, 255))
                window.blit(bed, (100, 250))


            display.update()
        else:
            finish = False
            score = 0
            miss = 0
            for i in monsters:
                i.kill()

            time.delay(3000)
            for i in range(5):
                monster = Enemy('ufo.png', randint(0, 635),-65,randint(1,5),80,80)
                monsters.add(monster)









            

        
        
        time.delay(20)