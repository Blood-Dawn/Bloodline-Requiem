# BLOODLINE REQUIEM - QUICK IMPLEMENTATION GUIDE

## For Developers: How to Use the New Systems

---

## TABLE OF CONTENTS
1. [Adding XP After Missions](#1-adding-xp-after-missions)
2. [Triggering Rank-Ups](#2-triggering-rank-ups)
3. [Using Abilities in Combat](#3-using-abilities-in-combat)
4. [Creating New Origin Starts](#4-creating-new-origin-starts)
5. [Adding Codex Entries](#5-adding-codex-entries)
6. [Moon Phase & Blood Satiation](#6-moon-phase--blood-satiation)
7. [Common Patterns & Examples](#7-common-patterns--examples)

---

## 1. ADDING XP AFTER MISSIONS

After any mission, quest, or significant achievement, grant XP:

```choicescript
*comment Example: After defeating an enemy
The enemy falls. Victory is yours.

*gosub_scene rank_progression gain_xp 75 "Defeated Rogue Varkyr"

*comment This adds 75 XP and displays a message if amount >= 50
```

### XP Recommendations by Task Type:

| Task Type | XP Amount | Example |
|-----------|-----------|---------|
| Minor task | 25-50 | Deliver message, gather info |
| Standard mission | 75-100 | Defeat minor enemy, solve puzzle |
| Major mission | 150-250 | Boss fight, critical plot choice |
| Epic achievement | 300-500 | Capture Ecliptic Shard, unite factions |

---

## 2. TRIGGERING RANK-UPS

After granting XP, check for progression:

```choicescript
*comment After mission completion
*gosub_scene rank_progression gain_xp 100 "Mission Complete"
*gosub_scene rank_progression check_progression

*comment If player qualifies, rank-up ceremony triggers automatically
*comment If not, play continues normally
```

### Full Mission Complete Template:

```choicescript
*label mission_complete
You return victorious. The Guild Master nods approvingly.

*comment Grant rewards
*set AssassinGuild_relation +10
*gosub_scene rank_progression gain_xp 150 "Completed Guild Contract"

*comment Check if player ranks up
*gosub_scene rank_progression check_progression

*comment Continue story
*goto next_mission
```

---

## 3. USING ABILITIES IN COMBAT

Check for ability flags to offer special options:

```choicescript
*label combat_encounter
An enemy blocks your path. How do you respond?

*choice
    #Attack with your weapon
        *goto basic_attack

    *if (shadow_step)
        #Use Shadow Step to flank
            You dissolve into shadows, reappearing behind the enemy!
            *set cunning +2
            The enemy spins, too late. Your blade finds their back.
            *goto victory

    *if (crimson_storm) and (blood_satiation > 50)
        #Unleash Crimson Storm (requires recent feeding)
            Blood erupts from your veins in a devastating tempest!
            *set blood_satiation -30
            The enemy is shredded in seconds.
            *goto overkill_victory

    *if (moons_fury) and (moon_phase = "Full")
        #Channel Moon's Fury (Full Moon only)
            Lunar energy surges through you, granting overwhelming power!
            *set rage +10
            Your claws tear through armor like parchment.
            *goto lunar_victory

    *if (twilight_veil)
        #Use Twilight Veil to become invisible
            You merge shadow and moonlight, vanishing from sight.
            The enemy searches frantically. You strike from nowhere.
            *goto stealth_victory
```

### Ability Usage Best Practices:

1. **Check prerequisites** (rank, blood satiation, moon phase, etc.)
2. **Apply costs** (reduce blood_satiation, increase rage, etc.)
3. **Provide unique narrative** for each ability
4. **Reward creativity** (stat bonuses, alternate outcomes)

---

## 4. CREATING NEW ORIGIN STARTS

Example: Creating `origins/origin_noble.txt`

```choicescript
*comment NOBLE ORIGIN - Human Noble Start

*label noble_start
*set alignment "human"
*set rank "Minor Noble"
*set strength 50
*set agility 50
*set cunning 75
*set will 70
*set age "24"

You were born into privilege, the third child of House Ravencrest. While your siblings schemed for succession, you honed your mind—studying politics, magic theory, and the whispered truths about Veilfall's supernatural underbelly.

Tonight, your father summons you to his study. The air reeks of blood.

*choice
    #Enter cautiously
        You push the door open. Your father lies slumped over his desk, twin puncture wounds on his neck. A Varkyr assassination.
        *goto investigate_murder

    #Call the guards
        You shout for the household guard. They arrive quickly, securing the scene. But the investigation will be... complicated.
        *goto official_investigation

    #Flee the estate
        Something is wrong. Your instincts scream [i]trap[/i]. You slip out the servants' entrance into the night.
        *goto exile_start

*label investigate_murder
*comment Continue noble path investigating supernatural politics...

*label official_investigation
*comment Continue noble path with authorities...

*label exile_start
*comment Continue as disgraced noble turned survivor...
```

### Connect to Act 1:

```choicescript
*comment After origin setup
*set act 1
*set chapter 1

*comment Route to appropriate Act 1 scene
*if (alignment = "varkyrs")
    *goto_scene act1_varkyr varkyrs_route
*elseif (alignment = "lupine")
    *goto_scene act1_lupine lupine_route
*elseif (alignment = "forsaken")
    *goto_scene act1_forsaken_ng+ forsaken_route
*else
    *goto_scene act1_human human_route
```

---

## 5. ADDING CODEX ENTRIES

### Adding to `codex/codex_locations.txt`:

```choicescript
*label location_overview

[b]LOCATIONS OF VEILFALL[/b]

Choose a location to learn more:

*choice
    #Veilfall City
        *goto veilfall_city
    #Mirror Lake
        *goto mirror_lake
    #Whispering Pines Forest
        *goto whispering_pines
    #Crimson Spire
        *goto crimson_spire
    #Return to main codex
        *goto_scene codex_main codex_main

*label veilfall_city
[b]Veilfall - City of Veiled Shadows[/b]

Population: ~500,000 (estimated, including hidden supernaturals)
Established: 800 BW (Before War)
Current Ruler: King Aldric III (human)

The capital city serves as the nexus of power in this world. On the surface, it appears as a thriving medieval-renaissance metropolis with cobblestone streets, grand cathedrals, and bustling markets.

Beneath the surface, four factions vie for control:
• The Crown occupies the palace district
• Varkyr courts hide in the noble quarters
• The Assassin Guild operates from unmarked safehouses
• Forsaken dwell in the underground tunnels

Notable Districts:
• [b]The Gilded Quarter[/b] - Noble estates and vampire courts
• [b]The Undercroft[/b] - Forsaken tunnels and black markets
• [b]Cathedral Heights[/b] - Church stronghold with anti-supernatural wards
• [b]The Warren[/b] - Commoner slums where the Guild recruits

*choice
    #Learn about another location
        *goto location_overview
    #Return to codex
        *goto_scene codex_main codex_main
```

---

## 6. MOON PHASE & BLOOD SATIATION

### Moon Phase System:

Add to a "monthly update" scene or time-passage:

```choicescript
*label advance_moon_phase
*comment Cycles through moon phases

*if (moon_phase = "Full")
    *set moon_phase "Waning Gibbous"
*elseif (moon_phase = "Waning Gibbous")
    *set moon_phase "Last Quarter"
*elseif (moon_phase = "Last Quarter")
    *set moon_phase "Waning Crescent"
*elseif (moon_phase = "Waning Crescent")
    *set moon_phase "New"
*elseif (moon_phase = "New")
    *set moon_phase "Waxing Crescent"
*elseif (moon_phase = "Waxing Crescent")
    *set moon_phase "First Quarter"
*elseif (moon_phase = "First Quarter")
    *set moon_phase "Waxing Gibbous"
*elseif (moon_phase = "Waxing Gibbous")
    *set moon_phase "Full"

*return

*comment Usage:
*gosub advance_moon_phase
The moon transitions to [b]${moon_phase}[/b].
```

### Moon Phase Effects (Lupines):

```choicescript
*if (alignment = "lupine")
    *if (moon_phase = "Full")
        [i]The full moon blazes. Your power surges![/i]
        *comment Apply +50% to all lupine abilities in combat
    *elseif (moon_phase = "New")
        [i]The new moon dims your connection. You feel weaker.[/i]
        *comment Apply -30% to all lupine abilities
```

### Blood Satiation System (Varkyrs):

```choicescript
*label feed_on_victim
You sink your fangs into the victim's throat. Hot blood floods your senses.

*set blood_satiation +40
*if (blood_satiation > 100)
    *set blood_satiation 100

*set Bloodlust -20
*if (Bloodlust < 0)
    *set Bloodlust 0

*if (victim_type = "innocent")
    *set control -10
    The innocent's terror lingers in the blood. Your humanity erodes.
*else
    *set control +5
    You feel no remorse. This one deserved their fate.

*return
```

### Satiation Effects:

```choicescript
*comment At start of each scene with a Varkyr PC:

*if (alignment = "varkyrs")
    *set blood_satiation -5
    *comment Passive hunger over time

    *if (blood_satiation < 30)
        *set Bloodlust +10
        The thirst claws at your mind. Nearby heartbeats echo like drums.

    *if (blood_satiation < 10)
        You are [i]starving[/i]. The beast within screams for blood.
        *comment Severe penalties to control, high risk of frenzy
```

---

## 7. COMMON PATTERNS & EXAMPLES

### Pattern A: Faction-Dependent Dialogue

```choicescript
*if (alignment = "varkyrs")
    The vampire noble recognizes your kind immediately.
    "Ah, one of us. Welcome, ${rank}. The court has heard of you."

*elseif (alignment = "lupine")
    The vampire's nose wrinkles in disgust.
    "A [i]dog[/i]. You have thirty seconds to state your business before I call the guards."

*elseif (alignment = "forsaken")
    The vampire hisses, stepping back.
    "Abomination! Leave my presence, hybrid filth!"

*else
    The vampire regards you with predatory interest.
    "A mortal. How... quaint. Do you have a death wish, little one?"
```

### Pattern B: Ability Combo Attacks

```choicescript
*if (shadow_step) and (crimson_storm)
    #Combine Shadow Step + Crimson Storm for devastating ambush
        You teleport behind the enemy and immediately unleash Crimson Storm at point-blank range.

        The enemy has no time to react. Blood magic tears them apart from behind.

        [i]CRITICAL HIT! +100 XP[/i]

        *set blood_satiation -40
        *gosub_scene rank_progression gain_xp 100 "Devastating Combo"
        *goto victory
```

### Pattern C: Relationship-Gated Choices

```choicescript
*if (met_Rurik) and (Rurik_relation >= 60)
    #Ask Rurik for help
        The alpha owes you a favor. You call it in.

        His pack arrives within the hour, ready for battle.

        *set lupine_relation +10
        *goto pack_reinforcements

*if (met_Caius) and (forsaken_relation >= 75)
    #Request Caius's intervention
        Few would dare call upon Caius the Unbound, but your relationship grants privilege.

        He appears from shadow, heterochromatic eyes gleaming.

        "I will handle this personally."

        *goto caius_intervention
```

### Pattern D: Ecliptic Shard Quests

```choicescript
*label shard_quest_complete
You hold the [b]${shard_name} Shard[/b] of the Ecliptic Amulet. Power hums through the crystal.

*set ecliptic_shards_controlled +1
*set artifact true

*if (ecliptic_shards_controlled >= 2)
    You now control multiple shards. Their combined resonance is... intoxicating.

*if (ecliptic_shards_controlled >= 4)
    All four shards. The power to remake—or destroy—the world.

    *choice
        #Reunify the Ecliptic Amulet
            *goto amulet_reunification
        #Keep the shards separated
            *goto maintain_balance
```

---

## QUICK COMMAND REFERENCE

### Grant XP:
```choicescript
*gosub_scene rank_progression gain_xp [amount] "[reason]"
```

### Check for Rank-Up:
```choicescript
*gosub_scene rank_progression check_progression
```

### Call Ability Selection (Manual):
```choicescript
*gosub_scene varkyr_abilities varkyr_ability_select
*gosub_scene lupine_abilities_complete lupine_ability_select
*gosub_scene forsaken_abilities forsaken_ability_select
```

### Navigate Codex:
```choicescript
*goto_scene codex_main codex_main
*goto_scene codex_world timeline
*goto_scene codex_races varkyrs_entry
```

### Advance Moon Phase:
```choicescript
*gosub advance_moon_phase
*comment (Add this subroutine to your main game loop or time-passage scenes)
```

### Feed (Varkyr):
```choicescript
*set blood_satiation +40
*set Bloodlust -20
*comment Add your own feeding narrative
```

---

## TESTING CHECKLIST

Before releasing a new scene/feature:

- [ ] Test with all four alignments (varkyrs, lupine, forsaken, human)
- [ ] Verify ability flags work correctly
- [ ] Check rank-up triggers at appropriate XP thresholds
- [ ] Test moon phase effects (if Lupine content)
- [ ] Test blood satiation effects (if Varkyr content)
- [ ] Verify faction relation changes update correctly
- [ ] Test codex entries navigate correctly
- [ ] Check for undefined variable errors (use ChoiceScript IDE)
- [ ] Playtest full path from origin → Act 1 → Act 2

---

## DEBUGGING TIPS

### Common Errors:

**"Invalid expression: variable not found"**
→ Add the variable to `startup.txt` with `*create variable_name initial_value`

**"Scene not found"**
→ Add the scene filename (without .txt) to the `*scene_list` in startup.txt

**"Ability selection doesn't trigger"**
→ Verify you're calling `*gosub_scene [ability_file] [label]` not `*goto_scene`

**"Moon phase doesn't affect combat"**
→ Add conditional modifiers in your combat scenes:
```choicescript
*if (moon_phase = "Full") and (alignment = "lupine")
    *set temp_strength (strength * 1.5)
```

**"XP isn't tracking"**
→ Check you're calling `gain_xp` with correct syntax:
```choicescript
*gosub_scene rank_progression gain_xp 100 "Reason"
```

---

## FINAL NOTES

**File Organization:**
- Origin files → `origins/` directory
- Ability systems → `systems/` directory
- Codex entries → `codex/` directory
- Act content → `scenes/` or root directory

**Scene Naming Convention:**
- Origins: `origin_[type].txt` (origin_assassin, origin_noble)
- Act scenes: `act[number]_[faction].txt` (act1_varkyr, act2_common_hub)
- Systems: `[system_name].txt` (rank_progression, varkyr_abilities)
- Codex: `codex_[category].txt` (codex_world, codex_races)

**Consistency is Key:**
- Use `alignment` for faction ("varkyrs", "lupine", "forsaken", "human")
- Use `rank` for Varkyr ranks
- Use `lupine_rank` for Lupine ranks
- Use `forsaken_rank` for Forsaken ranks
- Keep ability boolean flags lowercase with underscores (shadow_step, not ShadowStep)

---

**Happy developing! May your code be clean and your branching paths many. 🌙🩸**

---

## NEED HELP?

Refer to:
- **REFACTORING_SUMMARY.md** - Complete overview of all changes
- **SYSTEM_FLOW.md** - Visual diagrams and architecture
- **This file** - Quick implementation patterns

Check existing files for examples:
- `systems/varkyr_abilities.txt` - How to structure ability choices
- `systems/rank_progression.txt` - How to handle rank-ups
- `codex/codex_world.txt` - How to write lore entries
