from ursina import *
from ursina.editor.level_editor import *

def main():
    app = Ursina(vsync=False)

    class Tree(Entity):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.model = 'cube'
            self.color = color.brown

            self.top = Entity(name='tree_top', parent=self, y=1.5, model='cube', color=color.green, selectable=True)
            LEVEL_EDITOR.entities.append(self.top)


    level_editor = LevelEditor()
    # level_editor.goto_scene(0,0)


    from ursina.prefabs.first_person_controller import FirstPersonController
    level_editor.class_menu.available_classes |= {'WhiteCube': WhiteCube, 'EditorCamera':EditorCamera, 'FirstPersonController':FirstPersonController}
    from ursina.shaders import ssao_shader
    # camera.clip_plane_far = 100
    # camera.clip_plane_near = 1
    # camera.shader = ssao_shader
    window.borderless=False
    app.run()


if __name__ == '__main__':
    main()

    