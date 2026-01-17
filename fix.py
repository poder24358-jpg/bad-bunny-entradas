path = 'index.html'
with open(path, 'r', encoding='utf-8-sig') as f:
    content = f.read()

# Reemplazos directos y simples
content = content.replace('<div class="testimonial-image-placeholder">Imagen aquí</div>', '<div class="testimonial-image-placeholder"><img src="images/bot1.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:10px;"></div>', 1)
content = content.replace('<div class="testimonial-image-placeholder">Imagen aquí</div>', '<div class="testimonial-image-placeholder"><img src="images/bot2.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:10px;"></div>', 1)
content = content.replace('<div class="testimonial-image-placeholder">Imagen aquí</div>', '<div class="testimonial-image-placeholder"><img src="images/bot3.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:10px;"></div>', 1)
content = content.replace('<div class="testimonial-image-placeholder">Imagen aquí</div>', '<div class="testimonial-image-placeholder"><img src="images/bot4.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:10px;"></div>', 1)
content = content.replace('<div class="testimonial-image-placeholder">Imagen aquí</div>', '<div class="testimonial-image-placeholder"><img src="images/bot5.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:10px;"></div>', 1)
content = content.replace('<div class="testimonial-image-placeholder">Imagen aquí</div>', '<div class="testimonial-image-placeholder"><img src="images/bot6.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:10px;"></div>', 1)
content = content.replace('<div class="testimonial-image-placeholder">Imagen aquí</div>', '<div class="testimonial-image-placeholder"><img src="images/bot7.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:10px;"></div>', 1)
content = content.replace('<div class="testimonial-image-placeholder">Imagen aquí</div>', '<div class="testimonial-image-placeholder"><img src="images/bot8.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:10px;"></div>', 1)
content = content.replace('<div class="testimonial-image-placeholder">Imagen aquí</div>', '<div class="testimonial-image-placeholder"><img src="images/bot9.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:10px;"></div>', 1)
content = content.replace('<div class="testimonial-image-placeholder">Imagen aquí</div>', '<div class="testimonial-image-placeholder"><img src="images/bot10.jpg" style="width:100%;height:100%;object-fit:cover;border-radius:10px;"></div>', 1)

with open(path, 'w', encoding='utf-8-sig') as f:
    f.write(content)
print('Listo')
