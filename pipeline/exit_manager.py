missing_tracks = {}

def update_exit(track_ids):

    current_tracks = set(track_ids)

    exited = []

    for track in list(missing_tracks.keys()):

        if track not in current_tracks:

            missing_tracks[track] += 1

            if missing_tracks[track] > 5:
                exited.append(track)

        else:
            missing_tracks[track] = 0

    for track in current_tracks:

        if track not in missing_tracks:
            missing_tracks[track] = 0

    return exited

