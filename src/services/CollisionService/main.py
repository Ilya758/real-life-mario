import pygame


class CollisionService:
    @staticmethod
    def handleVerticalCollisions(player, objects, dy):
        collidedObjects = []

        for obj in objects:
            if pygame.sprite.collide_mask(player, obj):
                if dy > 0:
                    player.rect.bottom = obj.rect.top
                    player.land()
                elif dy < 0:
                    player.rect.top = obj.rect.bottom
                    player.hitHead()

                collidedObjects.append(obj)

        return collidedObjects

    @staticmethod
    def collide(player, objects, dx):
        player.move(dx, 0)
        player.update()
        collidedObject = None

        for obj in objects:
            if pygame.sprite.collide_mask(player, obj):
                collidedObject = obj
                break

        player.move(-dx, 0)
        player.update()

        return collidedObject
