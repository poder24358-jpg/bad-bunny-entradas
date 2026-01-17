with open("index.html", "r", encoding="utf-8-sig") as f:
    content = f.read()

# Agregar sección de comentarios antes del modal
comentarios_html = '''
    <!-- Sección de Comentarios y Testimonios -->
    <section class="comments-section">
        <h2 class="comments-title">¿Quieres compartir tu experiencia?</h2>
        <p class="comments-subtitle">Deja tu comentario y sube una captura de pantalla para que sea revisado por nuestro equipo</p>
        
        <form id="commentForm" class="comment-form">
            <div class="form-group">
                <label for="userName">Tu nombre *</label>
                <input type="text" id="userName" name="userName" placeholder="Juan Pérez" required>
            </div>
            
            <div class="form-group">
                <label for="userComment">Tu comentario *</label>
                <textarea id="userComment" name="userComment" placeholder="Cuéntanos tu experiencia comprando entradas en nuestra plataforma..." rows="5" required></textarea>
            </div>
            
            <div class="form-group">
                <label for="captureUpload">Sube una captura de pantalla (Imagen o PDF) *</label>
                <div class="file-upload-area" id="fileUploadArea">
                    <input type="file" id="captureUpload" name="captureUpload" accept="image/*,.pdf" required>
                    <div class="upload-placeholder">
                        <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                            <polyline points="17 8 12 3 7 8"></polyline>
                            <line x1="12" y1="3" x2="12" y2="15"></line>
                        </svg>
                        <p>Haz clic para seleccionar o arrastra tu archivo aquí</p>
                        <span class="file-size">Máx. 5MB</span>
                    </div>
                    <span id="fileName" class="file-name"></span>
                </div>
            </div>
            
            <button type="submit" class="submit-btn">Enviar Comentario</button>
        </form>
    </section>

    <!-- Modal de confirmación -->
    <div id="successModal" class="success-modal">
        <div class="success-modal-content">
            <button class="modal-close" onclick="cerrarModalExito()">&times;</button>
            <div class="success-icon"></div>
            <h3>¡Gracias por tu comentario!</h3>
            <p>Tu comentario y captura serán revisados por nuestro equipo administrativo.</p>
            <p class="modal-info">Nos tomaremos el tiempo necesario para validar tu aporte.</p>
            <button class="modal-btn" onclick="cerrarModalExito()">Entendido</button>
        </div>
    </div>
'''

# Encontrar la posición antes del modal de imagen ampliada
posicion = content.find('    <!-- Modal para imagen ampliada -->')
if posicion != -1:
    content = content[:posicion] + comentarios_html + '\n' + content[posicion:]

with open("index.html", "w", encoding="utf-8-sig") as f:
    f.write(content)

print(" Sección de comentarios agregada")
