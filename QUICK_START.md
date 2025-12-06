# BLOODLINE REQUIEM - QUICK START GUIDE

**For when you return to development**

---

## 🚀 GETTING STARTED IN 5 MINUTES

### Step 1: Understand What's Done ✅

You now have:
- **89+ abilities** across 3 factions (Varkyr, Lupine, Forsaken)
- **Automated rank-up system** that grants abilities when players progress
- **5000+ words of lore** in an interactive codex
- **100+ new variables** tracking everything from XP to moon phases
- **8000+ words of documentation** explaining how it all works

### Step 2: What to Do Next 🎯

**Priority 1 (Critical):** Origin Selection
- Create `origins/origin_select.txt` - Let players choose their start
- See `IMPLEMENTATION_GUIDE.md` section 4 for template

**Priority 2 (High):** Integrate Rank Progression
- Edit `scenes/act1_varkyr.txt` to add:
```choicescript
*gosub_scene rank_progression gain_xp 100 "Completed Initiation"
*gosub_scene rank_progression check_progression
```

**Priority 3 (Medium):** Test Full Loop
- Origin → Mission → Rank-up → Choose abilities → Use in combat

### Step 3: Quick Reference 📖

**Need to understand the architecture?**
→ Read `SYSTEM_FLOW.md` (15 min read)

**Need to implement something specific?**
→ Read `IMPLEMENTATION_GUIDE.md` (find your pattern, 5 min)

**Need project status overview?**
→ Read `PROJECT_STATUS.md` (10 min read)

**Need complete refactoring details?**
→ Read `REFACTORING_SUMMARY.md` (30 min read)

---

## 📂 FILE QUICK REFERENCE

### I want to...

**...add a new Varkyr ability**
→ Edit `systems/varkyr_abilities.txt`
→ Find the rank section (e.g., `*label knight_abilities`)
→ Add your new *choice option

**...add a new Lupine ability**
→ Edit `systems/lupine_abilities_complete.txt`
→ Find the rank section and type (Wolf/Werewolf/Omega)
→ Add your new *choice option

**...add a new hybrid ability**
→ Edit `systems/forsaken_abilities.txt`
→ Find `*label forsaken_unique_tree`
→ Add your new ability with power_level check

**...add lore to the codex**
→ Edit `codex/codex_world.txt` (for history)
→ Edit `codex/codex_races.txt` (for race info)
→ Or create `codex/codex_factions.txt` (for new category)

**...create a new origin**
→ Create `origins/origin_[name].txt`
→ See `IMPLEMENTATION_GUIDE.md` section 4 for template
→ Set alignment, rank, and starting stats
→ Route to Act 1 at the end

**...grant XP in a scene**
→ Add: `*gosub_scene rank_progression gain_xp 100 "Reason"`

**...check for rank-up**
→ Add: `*gosub_scene rank_progression check_progression`

**...use an ability in combat**
→ Add: `*if (shadow_step)` then offer special choice
→ See `IMPLEMENTATION_GUIDE.md` section 3 for examples

**...add a new variable**
→ Edit `startup.txt`
→ Add: `*create variable_name initial_value`
→ Add to scene_list if it's a new scene file

---

## 🧪 TESTING COMMANDS

### Test in ChoiceScript IDE:

1. Open `index.html` in ChoiceScript directory
2. Test specific paths:
   - Varkyr path: Set `alignment = "varkyrs"`, `rank = "Commoner"`
   - Lupine path: Set `alignment = "lupine"`, `lupine_rank = "Omega"`
   - Forsaken path: Set `alignment = "forsaken"`, `forsaken_rank = "Initiate"`

### Quick Test Checklist:
- [ ] Can navigate to codex from stats screen?
- [ ] Can browse world history in codex?
- [ ] Can browse race entries in codex?
- [ ] Does Varkyr ability selection work?
- [ ] Does Lupine ability selection work?
- [ ] Does Forsaken ability selection work?

---

## 💡 COMMON TASKS

### Task: Add XP to a Mission

```choicescript
*label mission_complete
The target falls. Another contract fulfilled.

*comment Grant XP
*gosub_scene rank_progression gain_xp 100 "Assassinated Target"

*comment Check for rank-up
*gosub_scene rank_progression check_progression

*comment Continue story
*goto return_to_guild
```

### Task: Use an Ability in Combat

```choicescript
*label combat
The enemy charges. What do you do?

*choice
    #Attack normally
        *goto basic_attack

    *if (shadow_step)
        #Use Shadow Step
            You vanish into shadows and strike from behind!
            *goto stealth_victory

    *if (moons_fury)
        #Channel Moon's Fury
            Lunar power surges through you!
            *goto lunar_victory
```

### Task: Add a Codex Entry

```choicescript
*comment In codex/codex_locations.txt

*label mirror_lake
[b]Mirror Lake - The Shattered Pact Site[/b]

Once a sacred place where Varkyrs and Lupines met annually for the ritual of balance, Mirror Lake now stands as a haunted reminder of broken oaths.

The water itself is said to reflect not your face, but your true nature—a trait that makes it both revered and feared.

*choice
    #Return to locations
        *goto location_overview
```

---

## ⚠️ TROUBLESHOOTING

### Error: "Invalid expression: variable not found"
**Fix:** Add the variable to `startup.txt` with `*create var_name value`

### Error: "Scene not found: [scene_name]"
**Fix:** Add scene to `*scene_list` in `startup.txt`

### Issue: Abilities don't appear in combat
**Fix:** Check that the ability flag is `true` and you're using correct `*if` syntax

### Issue: Rank-up doesn't trigger
**Fix:** Verify XP thresholds in `rank_progression.txt` match your XP gains

### Issue: Codex link doesn't work
**Fix:** Ensure `choicescript_stats.txt` uses `*goto_scene codex_main codex_main`

---

## 🎯 TODAY'S RECOMMENDED TASK

**If you have 30 minutes:**
Create `origins/origin_select.txt` - The origin selection menu
- Copy template from `IMPLEMENTATION_GUIDE.md` section 4
- Add 3 origins: Assassin (use prologue), Varkyr (use act1_varkyr), Lupine (use act1_lupine)
- Test navigation

**If you have 1 hour:**
Integrate rank progression into `act1_varkyr.txt`
- Add XP grants after each scene
- Add progression check at scene end
- Test full Varkyr playthrough: Start → Crimson Spire → Rank up → Choose abilities

**If you have 2 hours:**
Complete the codex by creating `codex/codex_factions.txt`
- Add Varkyr Courts entry
- Add Lupine Packs entry
- Add Forsaken Enclave entry
- Add Assassin Guild entry
- Link from `codex_main.txt`

**If you have 4+ hours:**
Create all 3 priority origins:
1. `origins/origin_assassin.txt` (refactor prologue)
2. `origins/origin_varkyr.txt` (use act1_varkyr intro)
3. `origins/origin_lupine.txt` (use act1_lupine intro)

Then create `origins/origin_select.txt` and test all paths.

---

## 📊 PROGRESS TRACKER

### Phase 1: Core Systems ✅ COMPLETE
- [x] Ability systems (all factions)
- [x] Rank progression framework
- [x] Codex (world & races)
- [x] Documentation

### Phase 2: Integration 🔄 IN PROGRESS
- [ ] Origin selection menu
- [ ] Integrate rank-ups into Act 1
- [ ] Complete codex (factions, locations, characters)
- [ ] Test full gameplay loop

### Phase 3: Content 🔴 NOT STARTED
- [ ] All 7 origins
- [ ] Romance foundations
- [ ] Act 1 expansion
- [ ] Act 2 development

---

## 🔗 QUICK LINKS

| Document | Purpose | Read Time |
|----------|---------|-----------|
| **QUICK_START.md** (this file) | Get started fast | 5 min |
| **IMPLEMENTATION_GUIDE.md** | How to implement features | 15 min (reference) |
| **SYSTEM_FLOW.md** | Architecture & diagrams | 15 min |
| **PROJECT_STATUS.md** | Current project state | 10 min |
| **REFACTORING_SUMMARY.md** | Complete change details | 30 min |

---

## 💬 NEED HELP?

### Common Questions:

**Q: Where do I add new abilities?**
A: `systems/[faction]_abilities.txt` files

**Q: How do I grant XP?**
A: `*gosub_scene rank_progression gain_xp [amount] "[reason]"`

**Q: How do I trigger rank-ups?**
A: `*gosub_scene rank_progression check_progression`

**Q: Where's the lore?**
A: `codex/` directory - navigate via stats screen

**Q: How do I test changes?**
A: Use ChoiceScript IDE or quicktest

**Q: Which file controls variables?**
A: `startup.txt` - all *create statements

**Q: Where's the scene list?**
A: `startup.txt` - at the top, *scene_list

---

## ✨ REMEMBER

**The hard work is done.** You now have:
- Robust systems ✅
- Comprehensive lore ✅
- Clear documentation ✅
- Scalable architecture ✅

**Now just add content:**
- Origins (player starting points)
- Missions (what players do)
- Choices (consequences that matter)
- Narrative (bring the world to life)

**One scene at a time. One choice at a time.**

The foundation is solid. Build confidently. 🌙🩸

---

*Last Updated: December 5, 2025*
*Quick Start Guide v1.0*
