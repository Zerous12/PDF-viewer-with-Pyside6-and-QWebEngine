from PySide6.QtCore import Qt, QPointF, QVariantAnimation
from PySide6.QtGui import QColor, QPainter
from PySide6.QtWidgets import QWidget
import math

class WaitingCircle(QWidget):
    def __init__(self, parent=None, radius=21, segment_radius=7, colors=None):
        super().__init__(parent)
        self.setParent(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Widget)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_StaticContents, True)
        self.setWindowModality(Qt.NonModal)

        # Configuración de parámetros del círculo
        self.radius = radius
        self.segment_radius = segment_radius
        self.num_segments = 7  # Número de bolitas en el círculo
        self.angle = 0  # Ángulo de rotación inicial

        self.colors = colors or [
            QColor(0, 120, 215), QColor(0, 200, 50), QColor(0, 188, 212),
            QColor(255, 255, 0), QColor(255, 87, 34), QColor(244, 67, 54), QColor(156, 39, 176)
        ]
        self.segment_colors = [self.colors[i % len(self.colors)] for i in range(self.num_segments)]
        self.segment_positions = []  # Lista para almacenar posiciones precalculadas

        # Precalcular las posiciones relativas de los segmentos en un círculo unitario
        self.unit_circle_positions = []
        for i in range(self.num_segments):
            angle = i * (360 / self.num_segments)
            x = math.cos(math.radians(angle))
            y = math.sin(math.radians(angle))
            self.unit_circle_positions.append((x, y))

        # Ajustar tamaño del widget
        widget_diameter = 2 * (self.radius + self.segment_radius + 10)
        self.setFixedSize(widget_diameter, widget_diameter)       
        # Animación con QVariantAnimation
        self.animation = QVariantAnimation(self)
        self.animation.setStartValue(0)
        self.animation.setEndValue(360)
        self.animation.setDuration(1500)  # Duración de una rotación completa
        self.animation.setLoopCount(-1)  # Repetir indefinidamente
        self.animation.valueChanged.connect(self.update_animation)

    def start(self):
        """Inicia la animación y muestra el widget."""        
        self.animation.start()
        self.show()

    
    def stop(self):
        """Detiene la animación y cierra el widget."""        
        self.animation.stop()
        self.close()

    def closeEvent(self, event):
        """Asegura que la animación se detiene al cerrar."""
        self.animation.stop()
        super().closeEvent(event)

    def update_animation(self, value):
        """Actualiza el ángulo de animación y redibuja el widget de manera optimizada."""
        # Redondear el ángulo a valores pares para reducir la frecuencia de actualización
        new_angle = round(value / 2) * 2  # Redondea al múltiplo de 2 más cercano

        # Si el ángulo no ha cambiado significativamente, no hacer nada
        if new_angle == self.angle:
            return

        # Actualizar el ángulo
        self.angle = new_angle

        # Redibujar solo las áreas necesarias
        self.update()

    def paintEvent(self, event):
        """Dibuja el círculo de carga animado."""
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        painter.setBrush(Qt.NoBrush)
        painter.setPen(Qt.NoPen)

        center = self.rect().center()

        for i, (ux, uy) in enumerate(self.unit_circle_positions):
            # Aplicar rotación y escalado a las posiciones precalculadas
            angle_rad = math.radians(self.angle)
            dx = ux * math.cos(angle_rad) - uy * math.sin(angle_rad)
            dy = ux * math.sin(angle_rad) + uy * math.cos(angle_rad)
            x = center.x() + dx * self.radius
            y = center.y() + dy * self.radius

            painter.setBrush(self.segment_colors[i])  # Asignar color correspondiente
            painter.drawEllipse(QPointF(x, y), self.segment_radius, self.segment_radius)

        painter.end()

    def superposition(self, enabled: bool):
        if enabled:
            self._recenter()
            self.raise_()

    def showEvent(self, event):
        super().showEvent(event)
        self._recenter()

    def _recenter(self):
        """Centra el widget dentro de su ventana padre si existe."""
        if self.parent():
            parent_rect = self.parent().rect()
            self.move(
                parent_rect.center().x() - self.width() // 2,
                parent_rect.center().y() - self.height() // 2
            )
