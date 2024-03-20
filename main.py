import os
import zipfile

ranges = {
    1: "1.6.1-1.8.9",
    2: "1.9-1.10.2",
    3: "1.11-1.12.2",
    4: "1.13-1.14.4",
    5: "1.15-1.16.1",
    6: "1.16.2-1.16.5",
    7: "1.17.x",
    8: "1.18.x",
    9: "1.19-1.19.2",
    12: "1.19.3",
    13: "1.19.4",
    15: "1.20-1.20.1",
    18: "1.20.2",
    22: "1.20.3-1.20.4"
}

if (os.path.exists("out")):
    for f in os.listdir("out"):
        os.remove("out/" + f)
else:
    os.mkdir("out")

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 15, 18, 22]:
    with zipfile.ZipFile(f"out/disable-vignette-{ranges.get(i)}.zip", "w") as f:
        with open("pack.mcmeta") as meta:
            f.writestr("pack.mcmeta", meta.read().replace("${pack_format}", str(i)))
        f.write("assets/minecraft/textures/misc/vignette.png")
        f.write("license")
