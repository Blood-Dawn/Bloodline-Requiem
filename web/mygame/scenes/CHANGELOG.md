# BLOODLINE REQUIEM - CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.5.0] - 2025-12-05 - PHASE 1 COMPLETE

### 🎉 Major Milestone: Core Systems & Comprehensive Codex

This release represents the completion of Phase 1 refactoring, establishing the foundational systems for Bloodline Requiem's multi-faction dark fantasy experience.

### Added

#### 🎮 Ability Systems
- **Varkyr Ability Selection System** (`systems/varkyr_abilities.txt`)
  - 10 rank tiers (Commoner → Progenitor)
  - 44 unique abilities with detailed descriptions
  - Automatic inheritance (higher ranks get all lower abilities)
  - Choose-2 selection mechanic at each rank
  - Progenitor auto-unlocks 4 apex abilities

- **Lupine Ability Selection System** (`systems/lupine_abilities_complete.txt`)
  - 11 rank tiers (Turned Omega → Lunar Progenitor)
  - 3 type variants (Wolf-Only, Werewolf-Only, Omega Variant)
  - 38 unique abilities across types and ranks
  - Type-specific ability trees
  - 5 common abilities auto-granted to all Lupines

- **Forsaken Hybrid Ability System** (`systems/forsaken_abilities.txt`)
  - 7 unique hybrid abilities (Twilight Veil, War Form, Eclipse Ascendant, etc.)
  - Cross-tree learning from both Varkyr and Lupine pools
  - 5 power levels (Initiate → Eclipse Lord/Lady)
  - Dual-magic mechanics (blood + lunar simultaneously)

#### 🔄 Progression Systems
- **Automated Rank Progression** (`systems/rank_progression.txt`)
  - XP tracking for all 3 factions (varkyr_xp, lupine_xp, forsaken_xp)
  - Threshold-based rank-ups with requirements (XP, faction relations, achievements)
  - Ceremonial rank-up sequences with narrative flavor
  - Automatic ability selection triggers
  - Special endgame sequences (Progenitor Ascension, Alpha Sovereign, Eclipse Lord/Lady)
  - Integrated XP gain function with reason tracking

#### 📚 Lore & Codex
- **Codex Main Hub** (`codex/codex_main.txt`)
  - Central navigation for all lore categories
  - Quick access from stats screen
  - Ecliptic Amulet dedicated entry

- **Complete World History** (`codex/codex_world.txt` - 1500+ lines)
  - Era of the Pact (500 BW - 1 BW)
  - The Millennium War (1 BW - 0 AW) with complete timeline
  - Post-War Era (1 AW - 250 AW)
  - Era of Shadows (250 AW - 1000 AW)
  - Present Era (1500 AW)
  - Progenitor vs Origin Wolf final duel details
  - Mirror Lake ritual mechanics
  - Crimson Eclipse faction backstory
  - Forsaken emergence narrative
  - Major faction founding stories

- **Complete Race Encyclopedia** (`codex/codex_races.txt` - 2000+ lines)
  - **Varkyrs**: Biology, powers, rank hierarchy, The Embrace ritual, culture, bloodline variants
  - **Lupines**: Three types detailed, rank system, The Bite, first kill doctrine, pack dynamics
  - **Forsaken**: Sub-types (Vamp-Wolf/Wolf-Vamp), Caius the Unbound lore, hybrid powers, War Form
  - **Humans**: Factions, transformation paths, Assassin Guild details, potential
  - Comparative power charts
  - Detailed ability breakdowns by rank
  - Creation rituals for each race

#### 📖 Documentation Suite
- **QUICK_START.md** - 5-minute orientation guide
- **IMPLEMENTATION_GUIDE.md** - Developer patterns and examples (1800+ lines)
- **SYSTEM_FLOW.md** - Architecture diagrams and flow charts (1200+ lines)
- **PROJECT_STATUS.md** - Current metrics, roadmap, completion tracking (1500+ lines)
- **REFACTORING_SUMMARY.md** - Complete change details (2500+ lines)
- **FILE_MAP.txt** - Navigation reference and quick links
- **GIT_COMMIT_MESSAGE.txt** - Ready-to-use commit template
- **CHANGELOG.md** - This file

#### 🗂️ File Structure
- Created `systems/` directory for game mechanics
- Created `codex/` directory for lore database
- Created `origins/` directory (ready for multi-origin content)
- Created `legacy/` directory (ready for NG+ content)

#### 📊 Variables & Tracking
- Added **100+ new variables** to `startup.txt`:
  - `varkyr_xp`, `lupine_xp`, `forsaken_xp` - Experience tracking
  - `blood_satiation` - Varkyr feeding state (0-100)
  - `moon_phase` - 8-phase lunar cycle
  - `hybrid_stability` - Forsaken balance (0-100)
  - `packs_united` - Lupine territory control
  - `ecliptic_shards_controlled` - Endgame artifact tracking
  - `met_Caius` - Forsaken leader interaction flag
  - 89+ ability boolean flags (shadow_step, moons_fury, etc.)
  - Lupine type tracking (omega_variant, werewolf_only, wolf_only)
  - Forsaken type tracking (forsaken_type, forsaken_rank)
  - Additional Lupine abilities (scent_mastery, unity_of_packs, etc.)
  - Lunar Progenitor abilities (progenitor_lunar_avatar, etc.)

### Changed

#### Updated Core Files
- **startup.txt**
  - Updated `*scene_list` with 9 new system/codex scenes
  - Added 100+ variable initializations
  - Added comprehensive comments for variable categories
  - Organized variables by faction/system

- **choicescript_stats.txt**
  - Updated codex link from deprecated `codex_lore` to `codex_main`
  - Navigation now points to new multi-file codex system

### Deprecated

- `scenes/codex_lore.txt` - Replaced by comprehensive codex/ directory
- `lupine_abilities.txt` (root) - Superseded by `systems/lupine_abilities_complete.txt`

### Fixed

- Inconsistent variable naming (now using `alignment` consistently)
- Missing Forsaken ability tracking
- Incomplete Lupine rank progression
- Lack of codex integration with stats screen

### Technical Details

#### Lines of Code
- Total new code: **~8,000+ lines**
- Ability systems: ~1,500 lines
- Rank progression: ~500 lines
- Codex content: ~3,500 lines
- Documentation: ~8,000 words

#### System Architecture
- Modular ability selection (3 faction-specific files)
- Centralized rank progression (1 file handles all factions)
- Hub-and-spoke codex navigation
- Subroutine-based XP and progression checks

### Known Issues

- Origin selection menu not implemented (blocks multi-origin experience)
- Act 1 scenes don't call rank_progression.txt yet (manual rank-ups required)
- Codex incomplete: factions, locations, characters entries pending
- Active ability equip system not implemented (can't choose which 5 to use)
- Moon phase doesn't auto-advance (needs time-passage integration)
- Blood satiation passive drain not implemented in scenes
- Old `lupine_abilities.txt` still in scene_list (needs removal)

### Migration Notes

For existing saves:
- ⚠️ **BREAKING**: New variables may cause undefined errors in old saves
- Recommended: Start new game after updating
- All new ability flags default to `false` (safe for existing characters)

For developers:
- Read `IMPLEMENTATION_GUIDE.md` for new usage patterns
- Update any scene calling old `lupine_abilities` to use `lupine_abilities_complete`
- Integrate `rank_progression` into mission completion sequences

---

## [0.1.0] - Earlier - INITIAL IMPLEMENTATION

### Added
- Basic prologue (assassin guild start)
- Act 1 scene stubs (varkyr, lupine, human routes)
- Mission board system
- Hub city navigation
- Basic stat tracking
- Relationship system (13 NPCs defined)
- Faction relation tracking

### Initial Features
- Assassination guild intro sequence
- Three-path branching (Forsaken, Lupine, Varkyr investigation)
- Basic Varkyr interaction (act1_varkyr.txt with Lord Vaelis)
- Lupine encounter system (act1_lupine.txt with pack dynamics)
- Stat screen with core attributes

---

## [Unreleased] - PLANNED FOR NEXT RELEASES

### Phase 2: Multi-Origin & Integration (v0.6.0 - Planned)
- [ ] Origin selection menu (`origins/origin_select.txt`)
- [ ] Refactored assassin origin (`origins/origin_assassin.txt`)
- [ ] Varkyr origin start (`origins/origin_varkyr.txt`)
- [ ] Lupine origin start (`origins/origin_lupine.txt`)
- [ ] Forsaken origin start (`origins/origin_forsaken.txt`)
- [ ] Integration of rank_progression into all Act 1 scenes
- [ ] Complete codex entries (factions, locations, characters)
- [ ] First full playthrough test (origin → Act 1 complete)

### Phase 3: Act 1 Completion (v0.7.0 - Planned)
- [ ] Human noble origin
- [ ] Human commoner origin
- [ ] Hunter origin
- [ ] Expanded Act 1 content (10+ hours gameplay)
- [ ] Romance foundation scenes (first meetings for all 13 NPCs)
- [ ] Ability usage integrated into all combat scenes
- [ ] Moon phase system with time progression
- [ ] Blood satiation passive drain system
- [ ] First kill moral choice for Lupines

### Phase 4: Act 2 Development (v0.8.0 - Planned)
- [ ] War escalation content
- [ ] Ecliptic Amulet shard quests (4 major quest lines)
- [ ] Faction conflict missions
- [ ] Romance progression (approval gates, relationship scenes)
- [ ] Territory management (Duke+ Varkyrs, Alpha+ Lupines)
- [ ] Active ability equip system (choose 5 from unlocked)

### Phase 5: Act 3 & Endgame (v0.9.0 - Planned)
- [ ] Final confrontations
- [ ] Amulet reunification decision
- [ ] Multiple endings based on:
  - MC race & rank
  - Romantic partner(s)
  - Faction outcomes
  - Shard control
- [ ] Progenitor ascension path
- [ ] Lunar Progenitor ascension path
- [ ] Eclipse Lord/Lady ascension path
- [ ] Epilogue variations (20+ unique epilogues)

### Phase 6: Legacy Content (v1.0.0 - Full Release)
- [ ] New Game+ mode
- [ ] Play as Progenitor (flashback during Pact era)
- [ ] Play as Origin Wolf (flashback during Millennium War)
- [ ] Play as faction general (alternate war scenarios)
- [ ] Unlock all abilities mode
- [ ] Bonus origins (unique starts)

---

## Version History Summary

| Version | Date | Phase | Status |
|---------|------|-------|--------|
| 0.5.0 | 2025-12-05 | Phase 1 Complete | ✅ Released |
| 0.1.0 | Earlier | Initial | ✅ Released |
| 0.6.0 | TBD | Phase 2 | 🔴 Planned |
| 0.7.0 | TBD | Phase 3 | 🔴 Planned |
| 0.8.0 | TBD | Phase 4 | 🔴 Planned |
| 0.9.0 | TBD | Phase 5 | 🔴 Planned |
| 1.0.0 | TBD | Full Release | 🔴 Planned |

---

## How to Update

### From v0.1.0 to v0.5.0:

1. **Backup your project**
   ```bash
   cp -r bloodline-requiem bloodline-requiem-backup
   ```

2. **Pull/copy new files**
   - Add all files in `systems/` directory
   - Add all files in `codex/` directory
   - Replace `startup.txt`
   - Replace `choicescript_stats.txt`

3. **Update scene_list**
   - Ensure new scenes are in startup.txt scene_list
   - Remove deprecated scene references

4. **Test in ChoiceScript IDE**
   - Run quicktest
   - Test codex navigation
   - Test ability selection (manual trigger)

5. **Read documentation**
   - Start with `QUICK_START.md`
   - Review `IMPLEMENTATION_GUIDE.md` for new patterns

---

## Credits

**Project Lead**: Kheiven D'Haiti
**Systems Architect**: Claude (Anthropic)
**Engine**: ChoiceScript
**Documentation**: Comprehensive developer guides

---

## License

See LICENSE.md for details.

---

## Links

- **Documentation**: See root directory for all .md files
- **Issue Tracker**: https://github.com/anthropics/claude-code/issues (for Claude Code feedback)
- **ChoiceScript**: https://www.choiceofgames.com/make-your-own-games/choicescript-intro/

---

*Last Updated: December 5, 2025*
*Changelog Version: 1.0*
