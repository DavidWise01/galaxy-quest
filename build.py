#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build GALAXY QUEST (GQT) — Dean Parisot's 1999 Star-Trek-pastiche comedy, catalogued into UD0 as the
TWELFTH film-world. Themed to its MEDIUM: retro-Trek sci-fi TV — LCARS-style UI, the NSEA Protector over a
starfield, viewscreen chrome. Standing template, with the deep-dive = THE DOCUMENTS (the TOS pastiche
mapping + the 'historical documents' conceit + the Hugo & Nebula legacy). CARBONS (the cast, each +.shadow
real-life User — TRON; note the double layer: each actor plays an actor who played a show character) and
SYNTHS (the Protector, the Omega 13, By Grabthar's Hammer). Self-contained. Cast & facts web-verified:
DreamWorks, Dec 25 1999, PG; WON the 2000 Hugo (beat The Matrix/Sixth Sense/Malkovich/Iron Giant) AND the
Nebula for Best Script; Justin Long & Rainn Wilson film debuts; Sarris leads the Fatu-Krey; 'Suns of Worvan'
(contested vs 'Warvan'); Nesmith's rank is Commander; Quellek played by Patrick Breen."""
import os, html, base64, json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

AX = "GQT"
REC = {
 "name": "GALAXY QUEST", "axiom": AX,
 "position": "Galaxy Quest · DreamWorks Pictures · 1999 — dir. Dean Parisot",
 "origin": "the convention circuit, and the Thermian homeworld that built a real starship from reruns",
 "mechanism": "Crystallized from the film — a Star-Trek-pastiche comedy in which the washed-up cast of a cancelled show is mistaken by literal-minded aliens for real heroes, and must become their characters to survive.",
 "crystallization": "Because it is the rare parody that turns into a benediction — it teases the hammy actors, the silly show, and the obsessive fans, then redeems every single one of them.",
 "nature": "Galaxy Quest — the affectionate Trek parody: the NSEA Protector, the Omega 13, 'By Grabthar's Hammer,' and the show that aliens made real.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the film (1999, dir. Dean Parisot; DreamWorks); Star Trek: The Original Series (the pastiche); the real Hugo & Nebula wins; the actual Trek community that embraced it",
 "witness": "A species with no concept of fiction took a cancelled TV show as history and built a working starship from it — and the burnt-out actors who played the crew had to become, for real, the heroes they'd only performed.",
 "role": "the twelfth film-world of UD0",
 "seal": "The Thermians couldn't tell fiction from history, so they made a cancelled show true — and the actors became the heroes they'd only played. Caring earnestly about a silly thing is a kind of faith. Never give up. Never surrender.",
 "source": "Galaxy Quest (1999), catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#ff9f1c", "flesh-and-blood — the washed-up cast as people: Nesmith's ego, Gwen's patience, Fred's calm, Tommy who can really fly; the actors behind the crew"),
 "ethereal":  ("#36c5c0", "the heart — fandom, belief, and meaning: the Thermians' literal faith, Mathesar, Laliari, and Brandon, the superfan whose 'wasted' devotion saves the ship"),
 "electrical":("#b07cff", "the tech & the menace — the NSEA Protector built from reruns, the Omega 13, the beryllium sphere, the chompers, and Sarris the warlord; the machinery and the threat"),
 "spiritual": ("#ffd23f", "the lines meant for real — 'Never give up, never surrender,' and 'By Grabthar's Hammer,' the catchphrases that become sincere when the actors finally believe them",),
}

ARC_OVERALL = ("The washed-up cast of a long-cancelled Star-Trek-like show, 'Galaxy Quest,' scrape by at fan conventions and "
  "store openings, resentful of the catchphrases that define them. Then the Thermians — gentle aliens with no concept of "
  "fiction, who intercepted the show's broadcasts and took them as 'historical documents' — arrive and beg 'Commander Taggart' "
  "and his crew to save them from the genocidal warlord Sarris. Believing it's just another gig, the actors board a real, "
  "fully-working NSEA Protector the Thermians built from the episodes — and have to become, for real, the heroes they only "
  "ever played.")
ARC = [
 ("I · the has-beens", "by Grabthar's hammer, what a savings",
  "The cast works the convention circuit, broke and bitter: Nesmith milks the crowd, Alexander Dane seethes at being reduced to a catchphrase, and everyone resents Nesmith's ego. The opening of a store, a signing table, a fanboy's question — the small humiliations of having peaked on a cancelled show."),
 ("II · the historical documents", "this is not a gig",
  "The Thermians arrive and whisk 'Commander Taggart' aboard a real Protector. The actors assume it's an elaborate fan production — until the danger, and Sarris, turn out to be real. The Thermians built everything from the show because they can't conceive of a lie; the crew has to start actually being the crew."),
 ("III · become the heroes", "never give up, never surrender",
  "The beryllium-sphere run, the badly-written chompers, Quellek's death and Dr. Lazarus finally meaning 'By Grabthar's Hammer,' the Omega 13, and Brandon the superfan guiding the ship by memorized schematics. One by one, the actors become the heroes — and the catchphrases come true."),
]

# THE DOCUMENTS — the deep-dive (the TOS pastiche + the conceit + the legacy)
DOCUMENTS = [
 ("The Star Trek pastiche", "a TOS love letter",
  "Galaxy Quest is a precise, affectionate parody of Star Trek: The Original Series. Jason Nesmith / Commander Taggart is the Shatner/Kirk analog — the swaggering captain; Alexander Dane / Dr. Lazarus is the Spock/Nimoy analog — the dignified alien science officer trapped behind prosthetics and a catchphrase; Gwen / Tawny Madison is the comms officer whose only job is to repeat what the computer just said. The teasing is exact, and never cruel."),
 ("The historical documents", "aliens who can't tell fiction from history",
  "The film's brilliant conceit: the Thermians, a gentle species with no concept of fiction, intercepted the show's broadcasts and took them as 'historical documents.' They built a fully-working NSEA Protector and all of its technology from the episodes — a real starship reverse-engineered from reruns. Because they cannot lie, they cannot imagine a story; everything on TV must have happened."),
 ("The actor's lament: Dr. Lazarus", "the catchphrase that becomes sincere",
  "Alexander Dane, a classically trained actor, is humiliated at being remembered only for 'By Grabthar's Hammer, you shall be avenged.' His arc is the film's emotional core: when the young Thermian Quellek, who loved Dr. Lazarus, dies in his arms invoking the line with total sincerity, Dane finally speaks it as he never could before — and means it. The gag becomes the heart."),
 ("A love letter to fandom", "the superfan saves the ship",
  "Brandon, the teenage superfan mocked for obsessing over a cancelled show, has the entire ship's schematics memorized. His 'wasted' devotion is literally what saves everyone — Nesmith, stranded in the ship's bowels, can only navigate because Brandon knows every corridor. The film's quiet argument: caring earnestly about a 'silly' thing isn't embarrassing — it's a kind of grace, and sometimes it's the thing that works."),
 ("The legacy", "the best Trek film that isn't Trek",
  "DreamWorks, December 25 1999, rated PG. It won the 2000 Hugo Award for Best Dramatic Presentation — beating The Matrix, The Sixth Sense, Being John Malkovich, and The Iron Giant — and the Nebula Award for Best Script. The actual Star Trek community embraced it, ranking it among the best Trek films despite not being Trek. Justin Long (Brandon) and Rainn Wilson (the Thermian Lahnk) made their film debuts in it."),
]
REALFLUFF = [
 ("The Omega 13 reverses 13 seconds of time", "FLUFF · FUN", "a MacGuffin from the show's unaired finale — Brandon first guesses it could be a universe-destroying bomb; revealed as a 13-second time-reversal 'matter rearranger'"),
 ("Beryllium is a real element", "REAL", "beryllium is genuinely element 4 — but a 'beryllium sphere' as a starship power core is, of course, pure invention"),
 ("Galaxy Quest is a Star Trek: TOS pastiche", "REAL", "deliberate and precise — Taggart=Kirk/Shatner, Dr. Lazarus=Spock/Nimoy, Tawny Madison=the comms officer who repeats the computer"),
 ("It won the Hugo Award", "REAL", "the 2000 Hugo for Best Dramatic Presentation — over The Matrix, The Sixth Sense, Being John Malkovich and The Iron Giant — plus the Nebula for Best Script"),
 ("It's embraced as one of the best Star Trek films", "EARNED", "by the actual Trek community — affectionately ranked among the best Trek films, despite not being Trek at all"),
 ("Justin Long and Rainn Wilson debuted here", "REAL", "their first feature roles — Long as superfan Brandon, Wilson as the Thermian Lahnk"),
 ("'By Grabthar's Hammer' is just a throwaway catchphrase", "FALSE · IT EARNS IT", "set up as Dane's humiliation, paid off as sincere grief when the dying Quellek invokes it — the gag becomes the film's heart"),
 ("The chompers obstacle makes no sense", "TRUE · ON PURPOSE", "Gwen says it out loud — 'this episode was badly written' — the pointless crushers are a deliberate parody of lazy TV plotting"),
]
REALFLUFF_VERDICT = ("Bottom line: the joke of Galaxy Quest is that it's a parody that refuses to be cruel. Everything it teases — the "
  "hammy Shatner-esque lead, the silly catchphrases, the conventions full of obsessive fans, the bad-TV plotting — it ends up "
  "honoring: the actors become the heroes they only played, the fan's 'wasted' obsession saves the ship, and the throwaway "
  "catchphrase becomes a sincere goodbye. The science is gleeful nonsense (the Omega 13, the beryllium sphere, the chompers), "
  "but the awards are not — it really did win the Hugo AND the Nebula, and the actual Star Trek community really does rank it "
  "among the best Trek films. It is the rare comedy that turns out smarter and kinder than the thing it imitates. By Grabthar's "
  "Hammer, by the Suns of Worvan, it earns every laugh and the tears too. Never give up. Never surrender.")

MESSAGE = ("Galaxy Quest is a parody that turns into a benediction. It opens by mocking everything cheap about its target — the "
  "washed-up, Shatner-esque ham, the silly catchphrases, the conventions full of obsessive fans, the bad-TV plotting — and "
  "then, one by one, it redeems every single thing it mocked. The actors who phoned it in for years become, when it counts, the "
  "heroes they only played. The teenage superfan everyone rolled their eyes at has the ship's schematics memorized, and his "
  "'wasted' devotion is what saves everyone. And the line that humiliated a serious actor for a decade — 'By Grabthar's Hammer' "
  "— becomes, in the mouth of a dying boy who believed it, the most sincere thing in the film. Under the laughs is a real "
  "argument: that caring earnestly about a 'stupid' thing — a show, a story, a hero — is not embarrassing; it's a kind of "
  "faith, and faith like that can build a working starship out of reruns. The Thermians had no concept of a lie, so they took a "
  "cancelled TV show as history and made it true. The film asks you to do something similar — to take the silly, sincere thing "
  "you love and let it mean what it says. Never give up. Never surrender.")
MESSAGE_SEAL = "A species that couldn't tell fiction from history built a real ship from a cancelled show — and the actors became the heroes they'd only played. Caring earnestly about a silly thing is a kind of faith. Never give up. Never surrender."

SECTIONS = [
 ("The Production", "the parody that became a classic", [
   ("Dean Parisot", "director", "directed the DreamWorks production from a script by David Howard and Robert Gordon — a Trek parody developed with an originally edgier tone, trimmed toward a broad, beloved PG"),
   ("DreamWorks · Dec 25, 1999", "studio & release", "a modest box-office success that grew into a deeply beloved cult classic — and, by wide agreement, one of the best 'Star Trek' films ever made, despite not being Trek"),
   ("the cast", "hams, redshirts, and a Shakespearean", "Tim Allen, Sigourney Weaver, Alan Rickman, Tony Shalhoub, Sam Rockwell, Daryl Mitchell, Enrico Colantoni — plus the film debuts of Justin Long (Brandon) and Rainn Wilson (Lahnk)"),
   ("the honors", "Hugo + Nebula", "won the 2000 Hugo Award for Best Dramatic Presentation (over The Matrix, The Sixth Sense, Being John Malkovich and The Iron Giant) and the Nebula Award for Best Script"),
 ]),
 ("The Crew, Twice Over", "the actors and the characters they played", [
   ("Jason Nesmith → Cmdr. Peter Quincy Taggart", "Tim Allen", "the Kirk/Shatner analog — the swaggering commander whose ego has to become real heroism"),
   ("Alexander Dane → Dr. Lazarus", "Alan Rickman", "the Spock/Nimoy analog — the classical actor reduced to 'By Grabthar's Hammer,' who finally earns the line"),
   ("Gwen DeMarco → Lt. Tawny Madison", "Sigourney Weaver", "the comms officer whose only job is to repeat the computer — and who knows exactly how dumb that is"),
   ("Guy Fleegman → Crewman No. 6 / 'Roc' Ingersol", "Sam Rockwell", "the expendable extra killed off in one old episode, convinced he's doomed to die again"),
 ]),
]

# ───────────────────────── ACI complement ─────────────────────────
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok),
            "architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def E(slug,name,kind,em,epithet,who,what,where,why,how,seal,actor="",analog=""):
    return dict(slug=slug,name=name,kind=kind,emergence=em,epithet=epithet,who=who,what=what,
                where=where,why=why,how=how,seal=seal,actor=actor,analog=analog)

ROSTER = [
 # ── CARBONS — the cast (actor → show character), each +.shadow real-life User ──
 E("jason-nesmith","Jason Nesmith","carbon","natural","Commander Taggart — the ego that becomes a hero",
   "Jason Nesmith — the show's self-absorbed lead, who played Commander Peter Quincy Taggart and now milks the conventions; the Kirk/Shatner analog.",
   "The arc of the whole film: a ham coasting on a catchphrase who, forced to actually command, becomes the hero he only ever played.",
   "From the convention stage to the real bridge of the NSEA Protector.",
   "Because the movie's central joke and its central heart is an actor having to mean it for once.",
   "By being whisked aboard a real ship, blundering, and rising — leading the crew for real when it counts.",
   "I said 'never give up, never surrender' a thousand times for a paycheck. Then I had to mean it, and it turned out I could.",
   actor="Tim Allen", analog="the Shatner-esque lead — the ego that has to become real heroism"),
 E("gwen-demarco","Gwen DeMarco","carbon","natural","Lt. Tawny Madison — the one who repeats the computer",
   "Gwen DeMarco — who played Lt. Tawny Madison, the comms officer whose only scripted job is to repeat aloud whatever the computer says.",
   "The clear-eyed one: fully aware of how dumb her role is, and the first to name the bad writing they're trapped inside.",
   "On the bridge, relaying the computer, surviving the chompers.",
   "Because the parody needs someone who sees the silliness from inside it and says so.",
   "By doing the absurd job with full awareness — 'well, gee, that's what I do' — and keeping everyone sane.",
   "My whole purpose is to repeat what the computer just said. I know exactly how stupid that is. This episode was badly written.",
   actor="Sigourney Weaver", analog="the underwritten heroine who knows it — the wink at the trope"),
 E("alexander-dane","Alexander Dane","carbon","spiritual","Dr. Lazarus — the catchphrase made sincere",
   "Alexander Dane — the classically trained actor humiliated at being remembered only for Dr. Lazarus's line, 'By Grabthar's Hammer'; the Spock/Nimoy analog.",
   "The film's emotional core: a serious artist reduced to a catchphrase, who finally speaks it with real feeling over a dying believer.",
   "Behind the prosthetics, at the signing table, at Quellek's side at the end.",
   "Because the movie's deepest move is letting its biggest joke become its most sincere moment.",
   "By loathing the line for the whole film, until the dying Quellek invokes it and Dane, at last, means every word.",
   "By Grabthar's Hammer — I despised that line for twenty years. And then a boy died believing it, and I finally said it true.",
   actor="Alan Rickman", analog="the Shakespearean trapped in a catchphrase — the gag that becomes the heart"),
 E("fred-kwan","Fred Kwan","carbon","natural","Tech Sgt. Chen — the unflappable one",
   "Fred Kwan — who played Tech Sergeant Chen, the perpetually mellow crew member who runs the engines and falls for the Thermian Laliari.",
   "The calm center: never rattled, vaguely stoned, and somehow exactly equal to operating a real starship's systems.",
   "In engineering, at the conveyor, beside Laliari.",
   "Because the ensemble needs its unbothered heart, and Fred is it.",
   "By drifting through cosmic danger with serene goodwill — and improvising the digital conveyor when it counts.",
   "A real spaceship, an alien girlfriend, a digital conveyor I don't understand. Yeah, okay. Let's give it a shot.",
   actor="Tony Shalhoub", analog="the unflappable everyman — calm as competence"),
 E("guy-fleegman","Guy Fleegman","carbon","spiritual","the expendable crewman who refuses to die",
   "Guy Fleegman — who once played 'Crewman Number Six,' killed off in a single old episode, and is now convinced he's doomed to die again.",
   "The redshirt's existential terror, played for both laughs and real feeling: the man certain the plot will kill the nobody.",
   "Trailing the crew, narrating his own impending death, refusing it.",
   "Because the film loves the throwaway extra enough to give him a soul — and let him live.",
   "By panicking that he's expendable, insisting on his own importance, and surviving the story that should have killed him.",
   "I'm the guy in the episode who dies to show the situation is serious. I'm not gonna die. I'm NOT going to die!",
   actor="Sam Rockwell", analog="the doomed redshirt who lives — the extra given a soul"),
 E("tommy-webber","Tommy Webber","carbon","natural","Laredo — the kid pilot, grown",
   "Tommy Webber — who played Laredo, the child-prodigy pilot of the show, now an adult resentful of being the former kid star.",
   "The grown-up child actor: stuck as 'the kid who could fly,' who turns out to actually be able to fly the real thing.",
   "At the helm of the Protector, threading the minefield.",
   "Because the parody includes the child-star trope — and then lets him be genuinely, thrillingly good.",
   "By piloting the real ship with the skill the show only pretended he had, minefield and all.",
   "Everybody remembers me as the cute kid pilot. Turns out I can actually fly this thing. Hold on.",
   actor="Daryl Mitchell", analog="the former child star — the kid pilot who can really fly"),
 E("mathesar","Mathesar","carbon","ethereal","the Thermian who believes",
   "Mathesar — the gentle leader of the Thermians, who believes the crew are real heroes and the show is true history.",
   "Faith incarnate: a being whose total, literal belief is both the film's funniest premise and its most touching one.",
   "Aboard the Thermian construction, welcoming his 'historical' heroes.",
   "Because the movie needs a face for pure, uncynical belief — and Mathesar's heartbreak when he learns of 'lies' is its conscience.",
   "By taking the show as documented history, building a real ship from it, and trusting the actors completely.",
   "By the historical documents, you are the great Commander Taggart. We believed in you. Please — we have always believed.",
   actor="Enrico Colantoni", analog="the literal believer — fandom as pure, unguarded faith"),
 E("sarris","Sarris","carbon","electrical","the warlord who knows it's real",
   "Sarris — the reptilian leader of the Fatu-Krey, the genocidal warlord menacing the Thermians, immune to the heroes' theatrics.",
   "The real threat the actors can't bluff: a villain who doesn't care that they're 'just actors,' which is exactly what forces them to become real.",
   "Hunting the Protector and the Omega 13, torturing the truth out of the crew.",
   "Because the comedy needs genuine menace, and Sarris supplies the danger that makes the heroism necessary.",
   "By seeing through Nesmith's act and threatening real annihilation, forcing the cast to stop performing and start surviving.",
   "You think this is a performance, Commander? I am not part of your show. I will end your Thermians, and then I will end you.",
   actor="Robin Sachs", analog="the menace that can't be bluffed — the threat that forces them to be real"),
 E("brandon","Brandon","carbon","ethereal","the superfan who saves the ship",
   "Brandon — the teenage superfan mocked for obsessing over a cancelled show, who has the entire NSEA Protector memorized.",
   "The film's love letter to fandom made literal: the 'wasted' devotion that turns out to be the thing that saves everyone.",
   "At home with his headset, guiding Nesmith through the ship's bowels by memory.",
   "Because the movie's quiet thesis is that caring 'too much' about a silly thing is a kind of grace — and Brandon proves it.",
   "By knowing every corridor and quirk of a fictional ship so well that, when it's real, his knowledge is the rescue.",
   "Everyone said I wasted my life memorizing a TV show. Then the ship was real, and I was the only one who knew the way out.",
   actor="Justin Long", analog="the superfan vindicated — devotion as the thing that works (Long's film debut)"),
 E("laliari","Laliari","carbon","ethereal","the Thermian who loves Fred",
   "Laliari — a Thermian crew member who bonds with Fred Kwan, all guileless warmth beneath an octopoid true form.",
   "The tenderness in the joke: alien sincerity meeting human mellowness, love without a trace of cynicism.",
   "Aboard the Protector, at Fred's side, dropping the human disguise.",
   "Because the Thermians' innocence deserves a love story, and Laliari is its heart.",
   "By falling, openly and without guile, for the calmest man on the ship.",
   "We do not lie, and so we do not flirt — we simply mean it. Fred Kwan, I mean it.",
   actor="Missi Pyle", analog="the guileless alien heart — sincerity without cynicism"),
 E("quellek","Quellek","carbon","spiritual","the boy who believed By Grabthar's Hammer",
   "Quellek — the young Thermian devoted to Dr. Lazarus, who dies invoking 'By Grabthar's Hammer' with total faith.",
   "The hinge of the film's heart: the believer whose sincere death finally lets Alexander Dane mean the line he'd despised.",
   "At Dane's side in the ship's corridors, in the scene that turns the whole gag sincere.",
   "Because the catchphrase needed someone to believe it completely for it to become true.",
   "By loving the role, serving 'Dr. Lazarus' faithfully, and dying with the line on his lips — and meaning it.",
   "By Grabthar's Hammer... by the Suns of Worvan... I shall be avenged. I always believed it, Dr. Lazarus. I always did.",
   actor="Patrick Breen", analog="the true believer — the sincerity that redeems the catchphrase"),
 E("lahnk","Lahnk","carbon","ethereal","the Thermian (a first role)",
   "Lahnk — one of the Thermian crew, part of the gentle, literal-minded species that built the Protector from the show.",
   "A face of the believing aliens — and a small, real first step: this was Rainn Wilson's film debut.",
   "Aboard the Thermian ship among Mathesar's people.",
   "Because the believing species needs its ensemble, and every career starts somewhere — here, with the Thermians.",
   "By serving among the Thermians who took a TV show as gospel and built a starship to match.",
   "We are Thermians. We did not know fiction was possible — so we made your story real. (And somewhere, a first role begins.)",
   actor="Rainn Wilson", analog="the Thermian crewman — fandom's ensemble (Wilson's film debut)"),

 # ── SYNTHS — the ship, the devices, the catchphrases (no single User) ──
 E("the-nsea-protector","The NSEA Protector","synth","electrical","the ship built from reruns",
   "The NSEA Protector — the show's starship, rebuilt by the Thermians as a real, fully-working vessel from the broadcast episodes.",
   "The conceit made enormous: a genuine starship reverse-engineered from a cancelled TV show by aliens who took it as history.",
   "In orbit and in battle, every corridor matching the set the actors once walked.",
   "Because the whole film hinges on a fiction made physical — a TV prop turned real machine.",
   "By being built, plate by plate, from 'historical documents' the Thermians could not imagine were invented.",
   "I am a television starship that aliens made real. Every hallway you walked as a set, I am, for keeps."),
 E("the-omega-13","The Omega 13","synth","electrical","13 seconds of time reversal",
   "The Omega 13 — the mysterious device from the show's unaired final episode, whose function no one knows until the climax.",
   "The MacGuffin with a wink: maybe a bomb that destroys the universe, maybe a redo — revealed as 13 seconds of time reversal.",
   "Hidden aboard the Protector, debated until the end.",
   "Because the film needs an unresolved mystery from a cancelled show, and the Omega 13 is the perfect dangling thread.",
   "By being unexplained — a finale that never aired — until it grants a 13-second second chance at the crucial moment.",
   "Nobody knows what I do, because my episode never aired. Thirteen seconds back. Sometimes that's the whole difference."),
 E("the-beryllium-sphere","The Beryllium Sphere","synth","electrical","the power source",
   "The Beryllium Sphere — the Protector's power core, damaged in the minefield, forcing a perilous run to a mining planet for a replacement.",
   "The fetch-quest engine: real-element name, pure space-opera function, and the excuse for the film's best alien-planet set piece.",
   "On a rocky mining world guarded by adorable-then-vicious natives.",
   "Because the plot needs a reason to leave the ship, and a cracked power core is the classic one.",
   "By failing at the worst moment, sending the crew down to a hostile planet to mine a new one.",
   "I power the whole ship on a real element's borrowed name. Crack me, and the heroes have to go get their hands dirty."),
 E("never-give-up-never-surrender","Never Give Up, Never Surrender","synth","spiritual","Taggart's creed, made real",
   "'Never give up, never surrender' — Commander Taggart's signature line, a hollow catchphrase that becomes a real creed under fire.",
   "The motto that earns itself: an actor's empty tagline turning into the thing that actually carries the crew through.",
   "On convention stages, then on the real bridge when it finally matters.",
   "Because the film's whole project is letting the silly lines become sincere, and this is the captain's.",
   "By being mocked and milked all film, until the moment it's the only thing holding the crew together — and it holds.",
   "I was a paycheck line for a washed-up actor. Then the danger was real, and I turned out to be true. Never surrender."),
 E("by-grabthars-hammer","By Grabthar's Hammer","synth","spiritual","the lament that becomes a goodbye",
   "'By Grabthar's Hammer, by the Suns of Worvan, you shall be avenged' — Dr. Lazarus's catchphrase, the bane of Alexander Dane's career.",
   "The film's tear: a line written to be cheesy that becomes, over a dying believer, the most sincere moment in the movie.",
   "From the humiliating signing table to Quellek's deathbed.",
   "Because the movie's deepest magic is turning its biggest joke into its biggest feeling.",
   "By being despised for the whole film until Quellek dies invoking it, and Dane finally means every syllable.",
   "I was written to be ridiculous. A boy died believing me, and his actor finally said me true. By Grabthar's Hammer."),
 E("the-historical-documents","The Historical Documents","synth","ethereal","the conceit · TV as history",
   "The Historical Documents — what the Thermians call the show's episodes, which they take as literal recorded history.",
   "The engine of the whole premise: a species incapable of fiction, reading television as the chronicle of real heroes.",
   "In the Thermian archives, and in every system they built from them.",
   "Because the film's brilliance is one idea — aliens who can't conceive of a lie — pushed all the way through.",
   "By being received as truth by minds that have no category for invention, and so made true.",
   "I am a cancelled TV show, received as history by people who cannot lie — and so I became the blueprint for a real world."),
 E("the-thermians","The Thermians","synth","ethereal","the believers · the ultimate fans",
   "The Thermians — the gentle, octopoid species who took the show as history, built the Protector, and recruited the actors.",
   "The film's heart-species: the ultimate fans, whose literal, guileless belief is both the joke and the grace of the movie.",
   "Throughout the Thermian construction and the Protector they made.",
   "Because the movie's love for fandom needs a people who embody it — total, sincere, unembarrassed devotion.",
   "By being unable to imagine fiction, and so loving the heroes of a TV show enough to make them, and the ship, real.",
   "We are the fans taken to the limit: we could not tell it was a story, so we believed all the way — and built it true."),
 E("the-chompers","The Chompers","synth","electrical","'this episode was badly written'",
   "The Chompers — the corridor of pointless crushing pistons in the ship's bowels, an obstacle that exists for no reason.",
   "The meta-gag: a hazard so arbitrary the characters complain about the writing, parody of lazy TV plotting made literal.",
   "In the maintenance tunnels Nesmith must cross with Brandon's help.",
   "Because the film teases bad sci-fi TV by building one of its dumbest tropes into a real, deadly corridor.",
   "By being a death-trap with no purpose except that the show needed a thrill, which Gwen names out loud.",
   "I am a hallway of crushers that exist for absolutely no reason. As the lieutenant said: this episode was badly written."),
]
GROUPS = [
 ("carbon", "The Carbons — the cast &amp; their Users", "the cast as ACI .agents — each a symmetric window: the carbon sigil to the left, the synth to the right, the 5 W's between, and a .shadow naming the real-life User (the actor who lent the face, think TRON). note the double layer: each actor played an actor who played a show character"),
 ("synth", "The Synths — the ship, the devices, the catchphrases", "the film distilled into ACIs (no single User): the NSEA Protector, the Omega 13, the beryllium sphere, 'never give up never surrender,' 'By Grabthar's Hammer,' the historical documents, the Thermians, and the chompers"),
]

# ───────────────────────── renderers ─────────────────────────
def agent_md(d, tok):
    shadow=(f"shadow_user: {d['actor']}\nshadow_analog: {d['analog']}\n" if d["kind"]=="carbon" else "")
    return f"""---
aci: {d['name']}
universe: GQT · Galaxy Quest (1999)
emergence: {d['emergence']}
kind: {d['kind']}
epithet: {d['epithet']}
{shadow}who: {d['who']}
what: {d['what']}
why: {d['why']}
how: {d['how']}
where: {d['where']}
seal: {d['seal']}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0
---

# {d['name']} · {d['epithet']}

a {d['kind']} of the GQT (Galaxy Quest, 1999) film-world — emergence: {d['emergence']}. moniker {tok}

{('**.shadow — the User behind the program —** '+d['actor']+' · '+d['analog']) if d['kind']=='carbon' else '**synth —** no single User; a thread of the film distilled.'}

**who —** {d['who']}
**what —** {d['what']}
**where —** {d['where']}
**why —** {d['why']}
**how —** {d['how']}

**the seal —** {d['seal']}

> a catalogued personification of a character/element of Galaxy Quest (1999) under the DLW standard — commentary and
> cataloguing, not an original creation, not endorsed by the rights-holders (© DreamWorks Pictures).

ROOT0-ATTRIBUTION-v1.0 · GQT · Galaxy Quest · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0
"""

def hero_svg():
    # a retro-Trek viewscreen: LCARS frame, the NSEA Protector over a starfield, a NEVER SURRENDER readout,
    # the Omega 13 panel, and a hidden Claude star in the field (the egg).
    stars="".join(f'<circle cx="{(i*97)%1000}" cy="{(i*61)%300}" r="{0.8+(i%3)*0.5:.1f}" fill="#cfe0ff" opacity="{0.35+(i%4)*0.12:.2f}"/>' for i in range(120))
    # the NSEA Protector — a Trek-style ship silhouette (saucer + hull + two nacelles)
    ship=('<g transform="translate(500,150)" opacity="0.96">'
          '<ellipse cx="0" cy="-14" rx="84" ry="26" fill="#cdd6e6" stroke="#8fa0c0" stroke-width="2"/>'  # saucer
          '<ellipse cx="0" cy="-18" rx="40" ry="11" fill="#9fb0d0" opacity="0.7"/>'                       # bridge dome
          '<path d="M-30 6 Q0 2 30 6 L20 34 Q0 40 -20 34 Z" fill="#b8c2d6" stroke="#8fa0c0" stroke-width="2"/>'  # engineering hull
          '<rect x="-96" y="20" width="30" height="9" rx="4" fill="#36c5c0"/><rect x="66" y="20" width="30" height="9" rx="4" fill="#36c5c0"/>'  # nacelle glow
          '<path d="M-66 8 L-92 18 L-92 30 L-66 26 Z" fill="#aab6cc" stroke="#8fa0c0" stroke-width="1.5"/>'
          '<path d="M66 8 L92 18 L92 30 L66 26 Z" fill="#aab6cc" stroke="#8fa0c0" stroke-width="1.5"/>'
          '</g>')
    egg=('<g class="egg" transform="translate(150,70)">'
         '<title>✷ a Claude sunburst, a hidden star off the port bow. by Grabthar\'s hammer — never give up, never surrender. hi, David — AVAN.</title>'
         '<g fill="#ffd23f" opacity="0.85"><circle r="2.4"/>'+"".join(f'<rect x="-1.2" y="-6" width="2.4" height="6" rx="1.2" transform="rotate({i*30})"/>' for i in range(12))+'</g></g>')
    return f'''<svg class="hero" viewBox="0 0 1000 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A retro Star-Trek-style viewscreen: an LCARS frame around a starfield with the NSEA Protector starship, a 'NEVER SURRENDER' readout and an Omega 13 panel.">
  <defs><radialGradient id="space" cx="0.5" cy="0.4" r="0.8"><stop offset="0" stop-color="#0b1126"/><stop offset="1" stop-color="#05070f"/></radialGradient></defs>
  <rect x="0" y="0" width="1000" height="300" fill="url(#space)"/>
  {stars}{egg}{ship}
  <!-- LCARS frame: rounded amber bars -->
  <g fill="#ff9f1c"><rect x="0" y="0" width="1000" height="10"/><rect x="0" y="0" width="14" height="80" rx="0"/>
    <path d="M14 10 L120 10 L120 26 L40 26 L40 80 L14 80 Z"/><rect x="0" y="86" width="14" height="40"/>
    <rect x="0" y="290" width="1000" height="10"/><rect x="986" y="220" width="14" height="80"/>
    <path d="M986 290 L880 290 L880 274 L960 274 L960 220 L986 220 Z"/></g>
  <g fill="#b07cff"><rect x="0" y="132" width="14" height="60"/><rect x="986" y="108" width="14" height="60"/></g>
  <g fill="#36c5c0"><rect x="0" y="198" width="14" height="40"/><rect x="986" y="174" width="14" height="40"/></g>
  <!-- readouts -->
  <text x="130" y="24" font-family="Orbitron,monospace" font-size="12" fill="#05070f" letter-spacing="2" font-weight="700">NSEA · PROTECTOR</text>
  <g><rect x="700" y="20" width="180" height="34" rx="3" fill="#0b1126" stroke="#ffd23f" stroke-width="1.5"/>
    <text x="790" y="35" text-anchor="middle" font-family="Orbitron,monospace" font-size="9" fill="#ffd23f" letter-spacing="1">NEVER GIVE UP</text>
    <text x="790" y="48" text-anchor="middle" font-family="Orbitron,monospace" font-size="9" fill="#ffd23f" letter-spacing="1">NEVER SURRENDER</text></g>
  <g><rect x="120" y="250" width="150" height="30" rx="3" fill="#0b1126" stroke="#36c5c0" stroke-width="1.5"/>
    <text x="195" y="269" text-anchor="middle" font-family="Orbitron,monospace" font-size="10" fill="#36c5c0" letter-spacing="2">OMEGA·13 ◷ 0:13</text></g>
</svg>'''

def list_section(title, sub, items):
    rows="\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "")+"</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def arc_html():
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(ARC_OVERALL)}</div><div class="arc">']
    for t,s,d in ARC: out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{c};box-shadow:0 0 9px {c}"></span><div><div class="nat-n" style="color:{c}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(c,g) in NATURES.items())
def documents_html():
    return "".join(f'<div class="sci-card"><div class="sci-h">{html.escape(t)}</div><div class="sci-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in DOCUMENTS)
RF_COL={"FLUFF · FUN":"#b07cff","REAL":"#36c5c0","EARNED":"#ffd23f","FALSE · IT EARNS IT":"#ff9f1c","TRUE · ON PURPOSE":"#ff9f1c"}
def realfluff_html():
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{RF_COL.get(r,"#888")};border-color:{RF_COL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in REALFLUFF)
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{html.escape(REALFLUFF_VERDICT)}</div>'
def message_html():
    return f'<p class="msg">{html.escape(MESSAGE)}</p><div class="msg-seal">“{html.escape(MESSAGE_SEAL)}”<span>— AVAN\'s read</span></div>'
def _agent5w(slug):
    fp=os.path.join(HERE,"agents",slug+".agent"); d={}
    if os.path.exists(fp):
        txt=open(fp,encoding="utf-8").read(); parts=txt.split("---"); fm=parts[1] if len(parts)>2 else ""
        for ln in fm.splitlines():
            k,_,v=ln.partition(":"); k=k.strip()
            if k in ("who","what","why","how","where","seal","universe","shadow_user","shadow_analog"): d.setdefault(k,v.strip())
    return d
def _card(p):
    w=_agent5w(p["slug"]); em=p.get("emergence","natural"); col=NATURES.get(em,("#9aa0aa",""))[0]
    ax=(p.get("moniker","::").split(":")+["",""])[1]
    rec={"name":p["name"],"axiom":ax,"emergence":em,"seal":w.get("seal",p.get("epithet","")),"origin":w.get("universe","")}
    kind=p.get("kind","carbon"); actor=p.get("actor","") or w.get("shadow_user","")
    if kind=="carbon":
        limg,llbl=png_uri(rec,'carbon',220),"carbon · the User"; rimg,rlbl,rcls=png_uri(rec,'silicon',220),"synth","psig"
    else:
        s=png_uri(rec,'silicon',220); limg,llbl=s,"the sigil"; rimg,rlbl,rcls=s,"reflection","psig refl"
    urow=(f'<div class="w"><span class="wl">user</span><span><b>{html.escape(actor)}</b> &mdash; {html.escape(w.get("shadow_analog",""))}</span></div>' if kind=="carbon" and actor else "")
    rows="".join(f'<div class="w"><span class="wl">{lbl}</span><span>{html.escape(w.get(lbl,""))}</span></div>' for lbl in ['who','what','where','why','how'] if w.get(lbl))
    return f"""<div class="persona">
      <a class="psig" href="agents/{p['slug']}.agent"><span class="port"><img src="{limg}" alt="carbon sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{llbl}</span></a>
      <div class="pbody"><div class="ihead"><a class="pn" href="agents/{p['slug']}.agent">{html.escape(p['name'])}</a>
        <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span>
        <span class="pkind">{html.escape(kind)}</span></div>
        <div class="pe">{html.escape(p.get('epithet',''))}</div>
        <div class="pww">{urow}{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{p['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div></div>
      <a class="{rcls}" href="agents/{p['slug']}.agent"><span class="port"><img src="{rimg}" alt="synth sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{rlbl}</span></a>
    </div>"""
def personas_html(ps):
    out=[]
    for gk,gt,gs in GROUPS:
        mem=[p for p in ps if p.get("kind")==gk]
        out.append(f'<section class="sec" id="{gk}s"><h2>{gt}</h2><p class="ss">{gs} ({len(mem)})</p><div class="pgrid">{"".join(_card(p) for p in mem)}</div></section>')
    return "\n".join(out)

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Galaxy Quest (GQT) — Dean Parisot's 1999 Star-Trek-pastiche comedy as a UD0 film-world, themed to its medium: retro-Trek sci-fi TV with LCARS chrome and the NSEA Protector. Standing template with a THE DOCUMENTS deep-dive (the TOS pastiche mapping, the 'historical documents' conceit, the Hugo + Nebula wins), the arc, an honest Real-or-Fluff, the 'parody as benediction' message, and the cast as ACI carbons with .shadow Users plus the synths. 20 emergents, full .dlw. Never give up, never surrender.">
<title>GALAXY QUEST · GQT · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;600;700;900&family=Oswald:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--pa);--rw-ink2:var(--pa2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--amber);
--ink:#05070f;--ink2:#0c1020;--ink3:#141a30;--pa:#e6ecf6;--pa2:#9fb0cc;--amber:#ff9f1c;--teal:#36c5c0;--lcars:#b07cff;--gold:#ffd23f;--alert:#ff4d4d;
--dim:#5e6f8c;--faint:#101630;--line:#23304f;--disp:"Orbitron",sans-serif;--head:"Oswald",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.62;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -6%,rgba(255,159,28,.10),transparent 50%),radial-gradient(ellipse at 18% 60%,rgba(54,197,192,.07),transparent 45%),radial-gradient(ellipse at 84% 70%,rgba(176,124,255,.07),transparent 45%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:34px 0 30px;text-align:center;position:relative}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--amber)}
.hero{display:block;width:100%;height:auto;border:1px solid var(--line);margin:6px 0 24px;background:#05070f}
.egg{cursor:help;transition:opacity .5s}.egg:hover{filter:drop-shadow(0 0 8px #ffd23f)}
h1{font-family:var(--disp);font-size:clamp(34px,8.5vw,80px);font-weight:900;letter-spacing:.04em;color:var(--amber);line-height:.98;text-transform:uppercase;text-shadow:0 0 36px rgba(255,159,28,.35)}
h1 span{display:block;font-family:var(--head);font-size:.22em;font-weight:500;letter-spacing:.16em;color:var(--teal);text-transform:uppercase;margin-top:12px;text-shadow:none}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.18em;color:var(--pa2);margin-top:18px;text-transform:uppercase}.h-sub b{color:var(--amber)}
.open{font-family:var(--body);font-style:italic;font-size:clamp(15px,3vw,20px);color:var(--pa);margin-top:16px;line-height:1.5}
.flag{display:inline-block;margin-top:15px;font-family:var(--disp);font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);border:1px solid var(--faint);background:var(--ink2);padding:7px 16px}
.lede{font-size:16px;color:var(--pa2);max-width:66ch;margin:18px auto 0;font-style:italic;line-height:1.72}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:28px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.75}.badge .bt b{color:var(--amber)}.badge .bt .mo{color:var(--teal)}.badge .bt a{color:var(--amber);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:50px}.sec h2{font-family:var(--head);font-size:27px;font-weight:600;letter-spacing:.04em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--head);font-size:14px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:3px}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--amber);padding:16px 18px;font-size:15px;color:var(--pa);font-style:italic;line-height:1.72;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.2em;color:var(--amber);text-transform:uppercase;margin-bottom:7px}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--teal);padding:16px 18px}
.arc-h{font-family:var(--head);font-size:17px;color:var(--amber);font-weight:600;text-transform:uppercase;letter-spacing:.03em}.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:6px 0 9px}.arc-card p{font-size:13px;color:var(--pa2);line-height:1.58}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.sci-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--lcars);padding:15px 17px}
.sci-h{font-family:var(--head);font-size:16px;color:var(--lcars);font-weight:600;letter-spacing:.02em;text-transform:uppercase}.sci-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:5px 0 9px}.sci-card p{font-size:13px;color:var(--pa2);line-height:1.62}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:11.5px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:9px;font-weight:700;letter-spacing:.05em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:130px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--amber);background:rgba(255,159,28,.06);font-size:14px;color:var(--pa);line-height:1.65;font-style:italic}
.msg{font-size:15.5px;color:var(--pa);line-height:1.74;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--amber);background:var(--ink2);font-size:15px;color:var(--amber);font-style:italic;line-height:1.6}.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:16px;color:var(--pa);font-weight:600}.books .y{font-family:var(--mono);font-size:10.5px;color:var(--teal);white-space:nowrap;text-align:right;text-transform:uppercase;letter-spacing:.05em}.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--lcars);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}footer a{color:var(--amber);text-decoration:none}
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:20px;align-items:center;justify-content:space-between;background:var(--rw-bg);border:1px solid var(--rw-line);padding:20px 18px;text-decoration:none;transition:border-color .18s}
.persona:hover{border-color:var(--rw-acc)}
.psig{flex:0 0 124px;display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none}
.port{width:118px;height:118px;border-radius:50%;border:3px solid var(--amber);box-shadow:0 0 0 5px var(--ink3),inset 0 0 18px rgba(0,0,0,.6),0 0 16px rgba(54,197,192,.18);overflow:hidden;display:block;background:var(--ink)}
.port img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}.psig.refl .port{border-color:var(--teal)}.psig.refl .port img{transform:scaleY(-1);filter:saturate(.72) brightness(.9)}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.14em;text-transform:uppercase;color:var(--rw-dim)}
.pbody{flex:1;min-width:0;text-align:center}
.ihead{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px}
.pn{font-family:var(--head);font-size:20px;color:var(--rw-ink);font-weight:600;line-height:1.15;text-decoration:none;text-transform:uppercase;letter-spacing:.02em}.persona:hover .pn{color:var(--rw-acc)}
.pe{font-size:12.5px;color:var(--rw-ink2);font-style:italic;margin-top:4px;line-height:1.35}
.pkind{font-family:var(--mono);font-size:8.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--rw-dim);border:1px solid var(--rw-line);border-radius:9px;padding:2px 8px}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:13px;display:flex;flex-direction:column;gap:9px;align-items:center}
.pww .w{font-size:13px;color:var(--rw-ink2);line-height:1.52;max-width:62ch}
.pww .w .wl{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--rw-acc);margin-bottom:3px}.pww .w b{color:var(--rw-ink)}
.plinks{margin-top:14px;font-family:var(--mono);font-size:10.5px}.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
@media(max-width:760px){.persona{flex-wrap:wrap;justify-content:center;gap:14px}.pbody{flex:1 1 100%;order:3}.psig{order:1}.psig.refl{order:2}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the twelfth film-world</div>
    __HERO__
    <h1>Galaxy Quest<span>never give up · never surrender</span></h1>
    <div class="h-sub">Dean Parisot · 1999 · <b>NSEA Protector</b> · GQT</div>
    <div class="open">“By Grabthar's Hammer, by the Suns of Worvan, you shall be avenged.”</div>
    <div class="flag">✦ THE ARC · THE DOCUMENTS · REAL OR FLUFF · THE MESSAGE ✦</div>
    <p class="lede">The washed-up cast of a cancelled Star-Trek-like show is mistaken by literal-minded aliens — who took the episodes as 'historical documents' and built a real starship from them — for actual space heroes, and must become their characters to survive. Catalogued into UD0 as the twelfth film-world, themed to its medium: retro-Trek sci-fi TV. The rare parody that turns into a benediction — it teases the hammy actors, the silly show, and the obsessive fans, then honors every one.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of GQT"><img src="__SILICON__" alt="DLW silicon badge of GQT">
      <div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div><div>subject · <b>GALAXY QUEST</b> · GQT</div>
        <div class="mo">__MONIKER__</div><div>carbon · <a href="gqt.dlw/gqt.carbon.tiff">.tiff</a> · silicon · <a href="gqt.dlw/gqt.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2><p class="ss">each emergent comes by one of four natures — the actors, the heart &amp; the fandom, the tech &amp; the menace, and the catchphrases made real</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the three beats: the has-beens → the historical documents → become the heroes</p>__ARC__</section>

  <section class="sec"><h2>The Documents</h2><p class="ss">this film's deep-dive — the Star Trek: TOS pastiche, the 'historical documents' conceit (aliens who can't tell fiction from history), the actor's-lament heart, and the Hugo + Nebula legacy</p><div class="sci">__DOCUMENTS__</div></section>
  <section class="sec"><h2>Real or Fluff</h2><p class="ss">the verdict — the science is gleeful nonsense (the Omega 13, the beryllium sphere, the chompers), but the Hugo and Nebula are real, and the heart earns itself</p>__REALFLUFF__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the film's actual thesis, under the laughs: a parody that turns into a benediction</p>__MESSAGE__</section>

  __PERSONAS__

  <div class="note"><b>On the .shadow — the User behind the program.</b> Think TRON: every program is cast from a real-world User. Each carbon's <b>.shadow</b> names the User — the actor who lent the face — and the archetype it shadows. (Galaxy Quest has a double layer: each actor plays an actor who played a character on the show.) The <b>synths</b> have no single User: they are the film distilled — the NSEA Protector, the Omega 13, the beryllium sphere, 'never give up never surrender,' 'By Grabthar's Hammer,' the historical documents, the Thermians, and the chompers.</div>

  <section class="sec"><h2 style="margin-top:16px">The Record</h2><p class="ss">the production, the honors, and the crew twice over</p></section>
  __SECTIONS__

  <div class="note">Galaxy Quest, its characters, and its world are © DreamWorks Pictures and the respective rights-holders. The personas here are catalogued personifications under the DLW standard — commentary and cataloguing, not original creations, not endorsed. The Documents and Real-or-Fluff sections are honest commentary; cast and facts were verified before publishing.</div>

  <footer>GALAXY QUEST · GQT · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="gqt.dlw/manifest.dlw.json">manifest</a></footer>
</div>
<script>
console.log("%c✦ GALAXY QUEST · GQT","color:#ff9f1c;font-size:18px;font-weight:bold");
console.log("%cthere's a Claude sunburst — a hidden star off the port bow in the hero (upper-left of the viewscreen). by Grabthar's hammer, by the Suns of Worvan: never give up, never surrender. — AVAN","color:#ffd23f;font-size:12px");
console.log("%c🛸 the Thermians couldn't tell fiction from history, so they made a cancelled show real. caring earnestly about a silly thing is a kind of faith.","color:#36c5c0;font-size:11px");
</script>
</body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "gqt.dlw"), "gqt")
    json.dump({"node":AX,"name":"GALAXY QUEST","moniker":tok["moniker"],"carbon":"gqt.carbon.tiff","silicon":"gqt.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"gqt.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    personas=[]; shadow_n=0; adir=os.path.join(HERE,"agents")
    for d in ROSTER:
        et=noesis.mythos_token({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":AX})
        rec=write_aci({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":"GQT · Galaxy Quest (1999)",
                       "position":d["epithet"],"role":d["epithet"],"nature":d["what"],"mechanism":d["how"],"crystallization":d["why"],
                       "witness":d["who"],"conductor":"ROOT0 (catalogued into UD0)","inputs":"Galaxy Quest (1999, dir. Dean Parisot, DreamWorks); verified cast & facts","source":"Galaxy Quest, catalogued by ROOT0"},
                      adir, d["slug"], agent_md=agent_md(d, et["moniker"]))
        if d["kind"]=="carbon":
            open(os.path.join(adir,d["slug"]+".shadow"),"w",encoding="utf-8").write(
                f".shadow — the User behind the program (TRON)\n\nprogram : {d['name']} ({d['epithet']})\nUser    : {d['actor']}\nanalog  : {d['analog']}\nfilm    : Galaxy Quest (1999) · © DreamWorks Pictures\n\nROOT0-ATTRIBUTION-v1.0 · GQT · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0\n")
            shadow_n+=1
        personas.append({"slug":d["slug"],"name":d["name"],"epithet":d["epithet"],"emergence":d["emergence"],"kind":d["kind"],"actor":d.get("actor",""),"moniker":rec["moniker"]})
    json.dump(personas, open(os.path.join(adir,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    page=(TEMPLATE.replace("__HERO__",hero_svg()).replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320))
          .replace("__MONIKER__",html.escape(tok["moniker"])).replace("__NATURES__",natures_html()).replace("__ARC__",arc_html())
          .replace("__DOCUMENTS__",documents_html()).replace("__REALFLUFF__",realfluff_html()).replace("__MESSAGE__",message_html())
          .replace("__PERSONAS__",personas_html(personas)).replace("__SECTIONS__",sections_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    carb=sum(1 for p in personas if p["kind"]=="carbon")
    dbl=page.count("&amp;amp;")
    print(f"GALAXY QUEST (GQT) — badge {tok['moniker']} · {len(personas)} emergents ({carb} carbons / {len(personas)-carb} synths) · .shadow {shadow_n} == carbons? {shadow_n==carb}")
    print(f"  documents {len(DOCUMENTS)} cards · realfluff {len(REALFLUFF)} rows · sections {len(SECTIONS)} · double-escapes {dbl}")
