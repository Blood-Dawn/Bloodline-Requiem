import os
import re

ROOT = os.path.dirname(os.path.dirname(__file__))


def get_scene_list(startup_path):
    scenes = []
    with open(startup_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    scene_list_started = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('*scene_list'):
            scene_list_started = True
            continue
        if scene_list_started:
            if not stripped or stripped.startswith('*'):
                break
            scenes.append(stripped)
    return scenes


def get_labels_and_gotos(path):
    labels = set()
    gotos = set()
    goto_re = re.compile(r'^\s*\*goto\s+(\S+)')
    label_re = re.compile(r'^\s*\*label\s+(\S+)')
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            m = label_re.match(line)
            if m:
                labels.add(m.group(1))
            m = goto_re.match(line)
            if m:
                gotos.add(m.group(1))
    return labels, gotos


def test_scene_files_exist():
    startup_path = os.path.join(ROOT, 'startup.txt')
    scenes = get_scene_list(startup_path)
    assert scenes, 'No scenes found in *scene_list'
    for scene in scenes:
        scene_file = os.path.join(ROOT, f'{scene}.txt')
        scene_alt = os.path.join(ROOT, 'scenes', f'{scene}.txt')
        assert os.path.isfile(scene_file) or os.path.isfile(scene_alt), \
            f"Scene file missing: {scene}"


def test_goto_targets_present():
    path = os.path.join(ROOT, 'act1_chapter1.txt')
    labels, gotos = get_labels_and_gotos(path)
    missing = [g for g in gotos if g not in labels]
    assert not missing, f"Missing labels for gotos: {missing}"
