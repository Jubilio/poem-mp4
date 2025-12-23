import os
from moviepy import TextClip, CompositeVideoClip, AudioFileClip, ImageClip, ColorClip
import moviepy.video.fx as vfx

# Versões do poema
FR_STANZAS = [
    "L’amour et l’adoration pour l’être aimé",
    "Sous les matins ensoleillés ou sous la lune éclatante,\nBinth Buque, ma muse, enchanteresse et rayonnante.\nDans tes yeux, le soleil reflète tout son éclat,\nEt la lune jalouse ta beauté, mon doux émoi.",
    "Dans ton étreinte, je trouve la chaleur du soleil,\nEt dans la douceur de ton sourire, la lune me conseille.\nTon amour est tel une éclipse, magique et singulière,\nUn instant éternel où tout devient lumière.",
    "Dans chaque vers que j’écris, dans chaque mot que je dis,\nJe célèbre l’amour qui nous unit, lien infini.\nBinth Buque, tu es l’étoile qui éclaire mon chemin,\nLa force qui me guide, à chaque pas, à chaque matin.",
    "Dans les strophes de ce poème, mon cœur se dévoile,\nCélébrant l’amour qui entre nous s’installe.\nJubílio Maússe, éternellement épris je suis,\nDe toi, Binth Buque, mon aimée, mon trésor infini."
]

PT_STANZAS = [
    "O amor e a adoração pela pessoa amada",
    "Nas manhãs ensolaradas ou sob o luar brilhante,\nBinth Buque, minha musa encantada e radiante.\nEm teus olhos, o sol reflete seu esplendor,\nE a lua inveja tua beleza, meu amor.",
    "No abraço teu, encontro a força do sol a me aquecer,\nE na suavidade do teu sorriso, a lua a me envolver.\nTeu amor é como um eclipse, mágico e singular,\nUm momento eterno onde tudo parece se acalmar.",
    "Em cada verso que escrevo, em cada palavra que digo,\nCelebro o amor que nos une, o elo que não tem abrigo.\nBinth Buque, és a estrela que ilumina o meu caminho,\nA força que me guia, em cada passo, em cada carinho.",
    "Nas estrofes deste poema, meu coração transparece,\nA celebração do amor que entre nós floresce.\nJubílio Maússe, apaixonado estou,\nPor ti, Binth Buque, minha amada, meu tesouro."
]

# Configurações
VIDEO_SIZE = (1280, 720)
FPS = 24
AUDIO_FILE = "someday.mp3"
BG_IMAGE = "fundo.png"
FONT_PATH = "C:/Windows/Fonts/Gabriola.ttf" 
if not os.path.exists(FONT_PATH):
    FONT_PATH = "C:/Windows/Fonts/georgia.ttf"

TOTAL_DURATION = 99
STANZA_DURATION = TOTAL_DURATION / len(FR_STANZAS)
CROSSFADE = 1.2

def create_bilingual_video():
    clips = []
    
    # 1. Fundo com Ken Burns
    if os.path.exists(BG_IMAGE):
        bg = ImageClip(BG_IMAGE).with_duration(TOTAL_DURATION).with_fps(FPS)
        bg = bg.with_effects([vfx.Resize(lambda t: 1 + 0.1 * t / TOTAL_DURATION)])
        bg = bg.with_position('center')
    else:
        bg = ColorClip(size=VIDEO_SIZE, color=(10, 10, 30)).with_duration(TOTAL_DURATION)
    
    overlay = ColorClip(size=VIDEO_SIZE, color=(0, 0, 0)).with_duration(TOTAL_DURATION).with_opacity(0.4)
    
    clips.append(bg)
    clips.append(overlay)

    # 2. Processar Estrofes Bilíngues
    current_time = 0
    for fr, pt in zip(FR_STANZAS, PT_STANZAS):
        # Clip Francês (Topo)
        txt_fr = TextClip(
            text=fr,
            font=FONT_PATH,
            font_size=55,
            color="white",
            size=(VIDEO_SIZE[0] - 250, None),
            method="caption",
            text_align="center"
        ).with_start(current_time).with_duration(STANZA_DURATION).with_position(('center', 150))
        
        # Clip Português (Baixo)
        txt_pt = TextClip(
            text=pt,
            font=FONT_PATH,
            font_size=42, # Um pouco menor para a tradução
            color="#E0E0E0", # Cinza claro para suavizar
            size=(VIDEO_SIZE[0] - 250, None),
            method="caption",
            text_align="center"
        ).with_start(current_time).with_duration(STANZA_DURATION).with_position(('center', 450))
        
        # Efeitos de Fade Sincronizados
        txt_fr = txt_fr.with_effects([vfx.FadeIn(CROSSFADE), vfx.FadeOut(CROSSFADE)])
        txt_pt = txt_pt.with_effects([vfx.FadeIn(CROSSFADE), vfx.FadeOut(CROSSFADE)])
        
        clips.append(txt_fr)
        clips.append(txt_pt)
        current_time += STANZA_DURATION

    # Compõe o vídeo
    video = CompositeVideoClip(clips, size=VIDEO_SIZE)
    
    # 3. Áudio
    if os.path.exists(AUDIO_FILE):
        print(f"A carregar áudio: {AUDIO_FILE}")
        audio = AudioFileClip(AUDIO_FILE).with_duration(TOTAL_DURATION).with_volume_scaled(0.15)
        video = video.with_audio(audio)
    
    print("A processar a sua obra-prima bilíngue...")
    video.write_videofile("declamacao_poesia.mp4", fps=FPS, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    create_bilingual_video()
