import genesis as gs

gs.init(backend=gs.gs_backend.cuda)


scene = gs.Scene()

scene.add_entity(
    morph=gs.morphs.URDF(
        file="terrain.urdf",
        pos=[0, 0, 0],
        fixed=True,
        scale=0.2,
    ),
    vis_mode="collision",
)

scene.build()

while True:
    scene.step()
