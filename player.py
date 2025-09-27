from circleshape import *
from constants import *
from shot import Shot

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.PLAYER_RADIUS = PLAYER_RADIUS
		self.rotation = 0
		self.shoot_timer = 0
	# in the player class
	def triangle(self):
	    forward = pygame.Vector2(0, 1).rotate(self.rotation)
	    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
	    a = self.position + forward * self.radius
	    b = self.position - forward * self.radius - right
	    c = self.position - forward * self.radius + right
	    return [a, b, c]
	def draw(self, screen):
		pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

	def rotate(self, dt):
		self.rotation += (PLAYER_TURN_SPEED* dt)
	
	def update(self, dt):
		keys = pygame.key.get_pressed()
		self.shoot_timer -= dt

		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
			self.shoot()
	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def shoot(self):
		new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
		velocity = pygame.Vector2(0, 1)
		velocity_rotate = velocity.rotate(self.rotation)
		new_shot.velocity = velocity_rotate * PLAYER_SHOOT_SPEED
		self.shoot_timer = PLAYER_SHOOT_COOLDOWN


