with open("index.html", "r", encoding="utf-8-sig") as f:
    content = f.read()

testimonios = '''    </main>

    <!-- Sección de Testimonios -->
    <section class="testimonials-section">
        <h2 class="testimonials-title">Lo que dicen nuestros clientes</h2>
        <div class="testimonials-container">
            <div class="testimonial-card">
                <h3 class="testimonial-name">Sol Ramires</h3>
                <p class="testimonial-text">Recomiendo la página mis entradas me aparecen sin problema</p>
                <div class="testimonial-image-placeholder">Imagen aquí</div>
            </div>
            <div class="testimonial-card">
                <h3 class="testimonial-name">Carlos Nestor</h3>
                <p class="testimonial-text">Sacamos con mi pareja recién antes que se agoten todas las entradas</p>
                <div class="testimonial-image-placeholder">Imagen aquí</div>
            </div>
            <div class="testimonial-card">
                <h3 class="testimonial-name">María González</h3>
                <p class="testimonial-text">Excelente experiencia comprando, muy fácil el proceso y rápido</p>
                <div class="testimonial-image-placeholder">Imagen aquí</div>
            </div>
            <div class="testimonial-card">
                <h3 class="testimonial-name">Juan Pérez</h3>
                <p class="testimonial-text">Las mejores entradas disponibles, servicio confiable y seguro</p>
                <div class="testimonial-image-placeholder">Imagen aquí</div>
            </div>
            <div class="testimonial-card">
                <h3 class="testimonial-name">Laura Martínez</h3>
                <p class="testimonial-text">Muy buena plataforma, recomendado para conseguir entradas confiables</p>
                <div class="testimonial-image-placeholder">Imagen aquí</div>
            </div>
            <div class="testimonial-card">
                <h3 class="testimonial-name">Diego López</h3>
                <p class="testimonial-text">Compré mis entradas en minutos, página muy intuitiva y segura</p>
                <div class="testimonial-image-placeholder">Imagen aquí</div>
            </div>
            <div class="testimonial-card">
                <h3 class="testimonial-name">Ana Rodríguez</h3>
                <p class="testimonial-text">Conseguí las entradas en el mejor precio, muy conforme con el servicio</p>
                <div class="testimonial-image-placeholder">Imagen aquí</div>
            </div>
            <div class="testimonial-card">
                <h3 class="testimonial-name">Roberto Fernández</h3>
                <p class="testimonial-text">Sistema muy seguro y confiable, mis entradas llegaron perfectas</p>
                <div class="testimonial-image-placeholder">Imagen aquí</div>
            </div>
            <div class="testimonial-card">
                <h3 class="testimonial-name">Valentina Silva</h3>
                <p class="testimonial-text">Impresionada con la facilidad de compra, definitivamente vuelvo</p>
                <div class="testimonial-image-placeholder">Imagen aquí</div>
            </div>
            <div class="testimonial-card">
                <h3 class="testimonial-name">Marcos Ruiz</h3>
                <p class="testimonial-text">Entradas legítimas y garantizadas, la mejor opción para comprar</p>
                <div class="testimonial-image-placeholder">Imagen aquí</div>
            </div>
        </div>
    </section>
'''

content = content.replace("</main>", testimonios)

with open("index.html", "w", encoding="utf-8-sig") as f:
    f.write(content)

print("Testimonios agregados exitosamente")
