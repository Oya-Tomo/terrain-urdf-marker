import argparse
import genesis as gs

parser = argparse.ArgumentParser(description="Terrain Viewer")
parser.add_argument(
    "--path",
    type=str,
    default="pyramid_terrain.urdf",
    help="Path to the URDF file of the terrain",
)
args = parser.parse_args()

gs.init(backend=gs.gs_backend.cuda)

scene = gs.Scene()
scene.add_entity(
    morph=gs.morphs.URDF(
        file=args.path,
        pos=[0, 0, 0],
        fixed=True,
        scale=0.2,
    ),
    vis_mode="collision",
)
scene.build()

while True:
    scene.step()
