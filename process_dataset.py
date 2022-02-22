import music21 as m21
from music21 import corpus, common
import json
import os


ALL_BACH_COMPOSITIONS = corpus.getComposer('bach')
SAVE_DIR = "dataset"
MAPPING_PATH = "mapping.json"
SEQUENCE_LENGTH = 64

# durations are expressed in quarter length
ACCEPTABLE_DURATIONS = [
    0.25, # 16th note
    0.5, # 8th note
    0.75,
    1.0, # quarter note
    1.5,
    2, # half note
    3,
    4 # whole note
]


def load_songs(dataset_list):
    """Loads all music pieces in dataset using music21.
    :param dataset_list (list): List containing music21.corpus paths
    :return songs (list of m21 streams): List containing all pieces
    """
    print("Total number of Bach pieces to process from music21: %i" % len(dataset_list))
    print(dataset_list)

    skipped = 0
    processed = 0

    songs = []

    # go through all the files in dataset and load them with music21
    for i, path in enumerate(dataset_list):
        path = common.cleanpath(path, returnPathlib=False)
        if "riemenschneider" in path:
            # skip certain files we don't care about
            print("Skipping undesired file %i, %s" % (i, path))
            skipped += 1
            continue

        p = corpus.parse(path)
        if len(p.parts) != 4:
            print("Skipping file %i, %s due to undesired voice count" % (i, path))
            skipped += 1
            continue
        print("Processing file %i, %s" % (i, path))
        processed += 1
        song = m21.converter.parse(path)
        songs.append(song)

    print(f"\n{processed} files processed")
    print(f"{skipped} files skipped")
    
    return songs



def main():
    songs = load_songs(ALL_BACH_COMPOSITIONS)
    song = songs[0]
    song.show()


if __name__ == "__main__":
    main()