import pygame

from constants import PLAYER_VEL
from services.CollisionService import CollisionService


class MovementService:
    @staticmethod
    def handleMove(player, objects):
        keys = pygame.key.get_pressed()
        player.x_vel = 0
        collideLeft = CollisionService.collide(
            player, objects, -PLAYER_VEL * 2)
        collideRight = CollisionService.collide(
            player, objects, PLAYER_VEL * 2)

        if keys[pygame.K_LEFT] and not collideLeft:
            player.move_left(PLAYER_VEL)
        if keys[pygame.K_RIGHT] and not collideRight:
            player.move_right(PLAYER_VEL)

        verticalCollide = CollisionService.handleVerticalCollisions(
            player, objects, player.y_vel)
        toCheck = [collideLeft, collideRight, *verticalCollide]

        for obj in toCheck:
            if obj and obj.name == 'fire':
                player.makeHit()
