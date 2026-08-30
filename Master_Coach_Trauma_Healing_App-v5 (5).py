import streamlit as st
import time

# ==============================================================================
# PAGE CONFIGURATION (MOBILE & PREMIUM PORTRAIT DESIGN)
# ==============================================================================
st.set_page_config(
    page_title="Master Coach: Trauma & Blockage Healing Companion V3",
    page_icon="👑",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# REUSABLE WEB SPEECH API TEXT-TO-SPEECH (TTS) COMPONENT
# ==============================================================================
def text_to_speech_button(text_to_speak, button_label="🔊 Dengarkan Suara Master Coach", language="id-ID"):
    # Escape quotes and formatting for JS
    escaped_text = (
        text_to_speak
        .replace("'", "\'")
        .replace('"', '\"')
        .replace("\\n", " ")
        .strip()
    )
    html_code = """
    <style>
        .tts-container {
            margin-top: 10px;
            margin-bottom: 10px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }
        .tts-button {
            background: linear-gradient(135deg, #d4af37 0%, #aa821e 100%) !important;
            color: #06090c !important;
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.9rem;
            font-weight: 700;
            padding: 8px 16px;
            border-radius: 8px;
            border: 1px solid rgba(212, 175, 55, 0.4);
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(212, 175, 55, 0.15);
            transition: all 0.2s ease-in-out;
            width: 100%;
            max-width: 320px;
            text-align: center;
            outline: none;
        }
        .tts-button:hover {
            background: linear-gradient(135deg, #f6e0b3 0%, #d4af37 100%) !important;
            transform: translateY(-1px);
            box-shadow: 0 6px 18px rgba(212, 175, 55, 0.3);
        }
        .tts-button:active {
            transform: translateY(1px);
        }
        .fallback-container {
            display: none;
            background-color: rgba(212, 175, 55, 0.08);
            border-left: 3px solid #d4af37;
            padding: 10px 14px;
            border-radius: 6px;
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.8rem;
            color: #94a3b8;
            max-width: 350px;
            text-align: left;
            line-height: 1.4;
            box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);
        }
    </style>
    <div class="tts-container">
        <button class="tts-button" onclick="speakText()">__BUTTON_LABEL__</button>
        <div id="fallback-msg" class="fallback-container"></div>
    </div>
    <script>
        function speakText() {
            if (!window.speechSynthesis) {
                showFallback("Browser Anda tidak mendukung fitur suara otomatis ini.");
                return;
            }
            
            // Cancel any current speech synthesis
            window.speechSynthesis.cancel();
            
            var text = "__ESCAPED_TEXT__";
            var utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = "__LANGUAGE__";
            utterance.rate = 0.90; // Meditation pacing (slightly slower)
            utterance.pitch = 1.05; // Gentle, warm tone
            
            // Try to auto-select a native indonesian voice if available
            var voices = window.speechSynthesis.getVoices();
            for (var i = 0; i < voices.length; i++) {
                if (voices[i].lang.indexOf("__LANGUAGE__") !== -1) {
                    utterance.voice = voices[i];
                    break;
                }
            }
            
            var started = false;
            
            utterance.onstart = function() {
                started = true;
                var btn = document.querySelector('.tts-button');
                btn.innerHTML = "📢 Sedang Membacakan...";
                btn.style.background = "linear-gradient(135deg, #10b981 0%, #059669 100%)";
                btn.style.color = "#ffffff";
                
                var msg = document.getElementById("fallback-msg");
                if (msg) msg.style.display = "none";
            };
            
            utterance.onend = function() {
                var btn = document.querySelector('.tts-button');
                btn.innerHTML = "__BUTTON_LABEL__";
                btn.style.background = "linear-gradient(135deg, #d4af37 0%, #aa821e 100%)";
                btn.style.color = "#06090c";
            };
            
            utterance.onerror = function(event) {
                console.error("TTS Error:", event);
                showFallback();
            };
            
            try {
                window.speechSynthesis.speak(utterance);
                
                // Timeout check: if after 1.5 seconds it hasn't started playing, show fallback
                setTimeout(function() {
                    if (!started) {
                        showFallback();
                    }
                }, 1500);
            } catch(e) {
                console.error(e);
                showFallback();
            }
        }
        
        function showFallback(customMsg) {
            var btn = document.querySelector('.tts-button');
            btn.innerHTML = "💡 Membaca Mandiri (Suara Diblokir)";
            btn.style.background = "rgba(212, 175, 55, 0.15)";
            btn.style.color = "#d4af37";
            btn.style.border = "1px solid rgba(212, 175, 55, 0.3)";
            
            var msg = document.getElementById("fallback-msg");
            if (msg) {
                msg.innerHTML = customMsg || "💡 <b>Browser memblokir suara otomatis (Iframe Sandbox).</b><br>Jangan khawatir! Silakan baca teks meditatif di bawah ini secara mandiri dengan tempo lambat, tenang, dan penuh penghayatan batin. Efek keselarasan energinya tetap berjalan sempurna! 🙏✨";
                msg.style.display = "block";
            }
        }
    </script>
    """.replace("__BUTTON_LABEL__", button_label).replace("__ESCAPED_TEXT__", escaped_text).replace("__LANGUAGE__", language)
    import streamlit.components.v1 as components
    components.html(html_code, height=135)

# ==============================================================================
# PREMIUM ELEGANT THEMING & RESPONSIVE CUSTOM CSS
# ==============================================================================
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
    /* Premium dark obsidian & gold color palette */
    .stApp {{
        background-color: #06090c !important;
        background-image: radial-gradient(circle at 50% 20%, #0d161d 0%, #06090c 80%) !important;
        color: #e2e8f0 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}
    
    /* Clean text formatting with high contrast */
    p, li, span, label {{
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 1.05rem !important;
        line-height: 1.6 !important;
        color: #cbd5e1 !important;
    }}
    
    /* Header typography */
    h1 {{
        font-family: 'Playfair Display', serif !important;
        font-size: 2.3rem !important;
        color: #d4af37 !important; /* Premium Classic Gold */
        text-align: center;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin-top: 10px !important;
        margin-bottom: 5px !important;
    }}
    
    h2 {{
        font-family: 'Playfair Display', serif !important;
        font-size: 1.7rem !important;
        color: #d4af37 !important;
        border-bottom: 1px solid rgba(212, 175, 55, 0.2);
        padding-bottom: 8px;
        margin-top: 20px !important;
        margin-bottom: 15px !important;
    }}
    
    h3 {{
        font-family: 'Playfair Display', serif !important;
        font-size: 1.35rem !important;
        color: #f6e0b3 !important;
        font-weight: 600;
        margin-top: 15px !important;
        margin-bottom: 10px !important;
    }}

    /* Subtitle text */
    .app-subtitle {{
        text-align: center;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: #94a3b8 !important;
        font-size: 1rem !important;
        margin-bottom: 25px !important;
    }}
    
    /* Interactive Streamlit Tabs customized for elegant feel */
    div.stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
        background-color: rgba(15, 23, 42, 0.6);
        padding: 6px;
        border-radius: 12px;
        border: 1px solid rgba(212, 175, 55, 0.15);
        overflow-x: auto;
    }}
    
    div.stTabs [data-baseweb="tab"] {{
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        color: #94a3b8 !important;
        background-color: transparent !important;
        border-radius: 8px !important;
        padding: 10px 14px !important;
        border: none !important;
        transition: all 0.3s ease;
    }}
    
    div.stTabs [aria-selected="true"] {{
        color: #06090c !important;
        background-color: #d4af37 !important;
        box-shadow: 0 4px 12px rgba(212, 175, 55, 0.25) !important;
    }}
    
    /* Elegant Box Cards */
    .luxury-card {{
        background-color: rgba(15, 23, 42, 0.55);
        border: 1px solid rgba(212, 175, 55, 0.2);
        padding: 22px;
        border-radius: 16px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(8px);
    }}

    /* Interactive checklist styling */
    .stCheckbox {{
        background-color: rgba(15, 23, 42, 0.3);
        padding: 10px 14px;
        border-radius: 10px;
        border: 1px solid rgba(212, 175, 55, 0.05);
        margin-bottom: 8px !important;
        transition: all 0.2s ease;
    }}
    .stCheckbox:hover {{
        border-color: rgba(212, 175, 55, 0.2);
        background-color: rgba(15, 23, 42, 0.5);
    }}
    
    /* Beautiful Quote & Prayer container */
    .prayer-container {{
        background-color: rgba(15, 23, 42, 0.85);
        border-left: 3px solid #d4af37;
        padding: 24px;
        border-radius: 12px;
        font-family: 'Playfair Display', serif !important;
        font-size: 1.1rem !important;
        line-height: 1.7 !important;
        font-style: italic;
        color: #f8fafc;
        margin-top: 15px;
        margin-bottom: 15px;
        box-shadow: inset 0 2px 8px rgba(0,0,0,0.5);
    }}
    
    /* Premium touch-friendly large CTA buttons */
    .stButton>button {{
        width: 100% !important;
        background: linear-gradient(135deg, #d4af37 0%, #aa821e 100%) !important;
        color: #06090c !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        padding: 14px 20px !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.2) !important;
        transition: all 0.3s ease-in-out;
    }}
    
    .stButton>button:hover {{
        background: linear-gradient(135deg, #f6e0b3 0%, #d4af37 100%) !important;
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(212, 175, 55, 0.35) !important;
    }}
    
    /* Badge element */
    .badge {{
        display: inline-block;
        padding: 3px 10px;
        font-size: 0.75rem !important;
        font-weight: 700;
        text-transform: uppercase;
        border-radius: 20px;
        background-color: rgba(212, 175, 55, 0.15);
        color: #d4af37;
        border: 1px solid rgba(212, 175, 55, 0.3);
        margin-bottom: 10px;
    }}

    /* Coached bubble styling */
    .coach-bubble {{
        background-color: rgba(20, 30, 45, 0.75);
        border: 1px solid rgba(212, 175, 55, 0.25);
        border-left: 5px solid #d4af37;
        padding: 20px;
        border-radius: 0px 16px 16px 16px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# HEADER
# =============================================================================
st.markdown("<h1>👑 MASTER COACH V3</h1>", unsafe_allow_html=True)
st.markdown("<p class='app-subtitle'>Sistem Klinis & Spiritual Terpadu • Dr. Hawkins, Napoleon Hill, Kiyosaki & Einstein</p>", unsafe_allow_html=True)

# Initialize Session States
if "stage" not in st.session_state:
    st.session_state.stage = "welcome"
if "trauma_category" not in st.session_state:
    st.session_state.trauma_category = "Belum Dipilih"
if "somatic_symptom" not in st.session_state:
    st.session_state.somatic_symptom = ""
if "limiting_belief" not in st.session_state:
    st.session_state.limiting_belief = ""
if "emotional_feeling" not in st.session_state:
    st.session_state.emotional_feeling = ""
if "hawkins_score" not in st.session_state:
    st.session_state.hawkins_score = 0
if "ancestral_bound" not in st.session_state:
    st.session_state.ancestral_bound = "Tidak Tahu"
if "seft_wizard_step" not in st.session_state:
    st.session_state.seft_wizard_step = 0
if "alignment_percentage" not in st.session_state:
    st.session_state.alignment_percentage = 0

# =============================================================================
# MAIN NAVIGATION (ELEGANT TABS)
# =============================================================================
tabs = st.tabs([
    "🤝 Sesi Coaching",
    "💆‍♂️ Protokol SEFT Paten",
    "🎵 Frekuensi Terapi",
    "📝 Jurnal Deklaratif",
    "📅 Indeks Pemulihan"
])

# =============================================================================
# TAB 1: 🤝 SESI COACHING (DIAGNOSTIK MENDALAM)
# =============================================================================
with tabs[0]:
    if st.session_state.stage == "welcome":
        welcome_text = (
            "Selamat datang, Jiwa yang Hebat. Saya adalah Master Coach Anda. "
            "Di ruangan sunyi ini, kita tidak hanya membahas permukaan masalah Anda, "
            "melainkan menyelam langsung ke dasar batin untuk menemukan akar dari segala trauma, "
            "kecemasan, atau hambatan hidup yang membelenggu Anda. "
            "Mari kita selaraskan kembali energi Anda menuju kelimpahan sejati."
        )
        
        st.markdown("""
        <div class='coach-bubble'>
            <h3>"Selamat datang, Jiwa yang Hebat."</h3>
            <p>Saya adalah <b>Master Coach</b> Anda. Di ruangan sunyi ini, kita tidak hanya akan membahas permukaan masalah Anda, melainkan menyelam langsung ke dasar batin Anda untuk menemukan akar dari segala trauma, kecemasan, atau hambatan hidup yang selama ini membelenggu potensi sejati Anda.</p>
            <p>Sesuai hukum fisika yang diutarakan oleh <b>Albert Einstein</b>: <i>"Segala sesuatu adalah energi. Selaraskan frekuensi realitas yang Anda inginkan, dan Anda tidak akan bisa menghindari realitas tersebut. Ini bukan filosofi, ini fisika."</i></p>
            <p>Setiap rasa sakit, kegagalan yang berulang, atau ketakutan yang Anda bawa memiliki <b>pola energetik, somatik, dan bawah sadar</b>. Tugas kita bersama hari ini adalah mendeteksi pola itu, membedahnya, lalu menghancurkannya secara paten hingga Anda terbebas sepenuhnya.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Add Voice TTS Button
        text_to_speech_button(welcome_text, "🔊 Dengarkan Suara Master Coach (Sapaan Awal)")
        
        if st.button("MULAI SESI DIAGNOSIS MENDALAM ➡️"):
            st.session_state.stage = "choose_category"
            st.rerun()

    elif st.session_state.stage == "choose_category":
        st.markdown("<h2>🔍 Langkah 1: Tentukan Area Hambatan Terbesar</h2>", unsafe_allow_html=True)
        st.write("Silakan pilih area kehidupan mana yang saat ini sedang mengalami kemacetan atau trauma terbesar:")
        
        category = st.radio(
            "Pilih Niche Masalah/Trauma Anda:",
            [
                "💔 Trauma Asmara & Luka Relasi (Brokenheart, Pengkhianatan, Takut Ditolak)",
                "💼 Sumbatan Karir, Bisnis, & Prestasi (Stagnasi, Imposter Syndrome, Prokrastinasi)",
                "🛡️ Krisis Kepercayaan Diri & Penolakan Diri (Rasa Bersalah, Malu, Merasa Tidak Layak)",
                "💸 Trauma Finansial & Mental Kelangkaan (Kendi Bocor, Cemas Uang, Takut Miskin)",
                "🏡 Trauma Pengasuhan & Luka Silsilah (Luka Batin Masa Kecil, Konflik Orang Tua)"
            ]
        )
        
        if st.button("Lanjutkan Penggalian Batin ➡️"):
            st.session_state.trauma_category = category
            st.session_state.stage = "somatic_scan"
            st.rerun()

    elif st.session_state.stage == "somatic_scan":
        st.markdown(f"<h2>🩺 Langkah 2: Pindai Sinyal Tubuh (Somatic Scan)</h2>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class='coach-bubble'>
            <p><b>Master Coach Analysis:</b> Area yang Anda pilih adalah <b>{st.session_state.trauma_category}</b>.</p>
            <p>Pikiran sadar Anda bisa berbohong, tetapi tubuh fisik Anda <b>tidak pernah berbohong</b>. Rasa sakit, beban, atau kecemasan emosional selalu direkam secara biologis oleh tubuh kita sebagai ketegangan fisik.</p>
            <p>Tutup mata Anda sejenak. Ambil napas dalam... embuskan. Pikirkan masalah atau trauma terbesar Anda di area ini. Di bagian tubuh mana Anda merasakan ketegangan, sesak, mulas, kaku, atau tidak nyaman?</p>
        </div>
        """, unsafe_allow_html=True)
        
        somatic = st.text_input(
            "Tuliskan area tubuh and rasa tidak nyaman yang Anda deteksi (Contoh: 'Dada terasa sesak bagai ditekan batu', atau 'Perut terasa kaku dan melilit'):",
            placeholder="Tuliskan di sini..."
        )
        
        somatic_tts_text = (
            "Tutup mata Anda sejenak. Ambil napas dalam, lalu embuskan secara perlahan. "
            "Pikirkan masalah Anda. Di bagian tubuh mana Anda merasakan ketegangan, sesak, mulas, kaku, atau tidak nyaman? "
            "Pikiran sadar Anda bisa berbohong, tetapi tubuh fisik Anda tidak pernah berbohong."
        )
        text_to_speech_button(somatic_tts_text, "🔊 Bimbingan Somatic Scan (Meditatif)")

        if st.button("Konfirmasi Sinyal Tubuh ➡️"):
            if somatic.strip() != "":
                st.session_state.somatic_symptom = somatic
                st.session_state.stage = "subconscious_lie"
                st.rerun()
            else:
                st.warning("Mohon tuliskan sensasi tubuh Anda terlebih dahulu agar Master Coach dapat merumuskan resep terapi yang presisi.")

    elif st.session_state.stage == "subconscious_lie":
        st.markdown("<h2>🧠 Langkah 3: Bongkar Kebohongan Bawah Sadar (The Lie)</h2>", unsafe_allow_html=True)
        
        # Integrate Kiyosaki wisdom for finance niche
        kiyosaki_note = ""
        if "💸" in st.session_state.trauma_category:
            kiyosaki_note = """
            <p style='color: #dfb15b; font-size: 0.95rem; font-style: italic;'>
                <b>Pesan Robert Kiyosaki:</b> Hambatan keuangan sejati bukan karena kurangnya uang kertas di dompet Anda, melainkan karena pikiran Anda masih memprogram pola pikir 'liabilitas' yang memeras energi hidup Anda. Kita harus menggeser batin Anda menjadi 'aset' spiritual berkelimpahan.
            </p>
            """

        st.markdown(f"""
        <div class='coach-bubble'>
            <p><b>Master Coach Analysis:</b> Sinyal tubuh Anda merekam ketegangan berupa: <i>\"{st.session_state.somatic_symptom}\"</i>.</p>
            {kiyosaki_note}
            <p>Sekarang kita masuk ke pikiran bawah sadar Anda. Setiap hambatan batin diciptakan oleh <b>kebohongan mental (limiting belief/asumsi salah)</b> yang Anda percayai sejak masa lalu atau masa kecil.</p>
            <p>Ketika Anda mengalami masalah ini, kebohongan negatif apa yang dibisikkan oleh batin Anda tentang diri Anda? (Contoh: 'Saya tidak akan pernah bahagia', 'Mencari uang itu menyiksa', 'Saya ditakdirkan gagal', atau 'Semua orang pasti meninggalkan saya').</p>
        </div>
        """, unsafe_allow_html=True)
        
        lie = st.text_area(
            "Tulis kebohongan batin yang merusak hidup Anda tersebut di sini:",
            placeholder="Tuliskan sejujur-jujurnya tanpa sensor..."
        )
        
        if st.button("Hancurkan Kebohongan Ini ➡️"):
            if lie.strip() != "":
                st.session_state.limiting_belief = lie
                st.session_state.stage = "emotional_debt"
                st.rerun()
            else:
                st.warning("Jangan menyembunyikan kebohongan itu. Tuliskan agar kita bisa membongkarnya bersama.")

    elif st.session_state.stage == "emotional_debt":
        st.markdown("<h2>🎭 Langkah 4: Kalibrasi Peta Kesadaran (Dr. David R. Hawkins)</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div class='coach-bubble'>
            <p>Berdasarkan buku legendaris <b>Power vs. Force</b> oleh <b>Dr. David R. Hawkins</b>, setiap emosi manusia memiliki frekuensi energi yang terkalibrasi secara ilmiah:</p>
            <p>• <b>Gaya Paksaan (Force / Vibrasi Rendah &lt; 200):</b> Menarik penderitaan, penyakit, dan kegagalan berulang karena sel tubuh bergetar dalam mode bertahan hidup (fear/surrender).</p>
            <p>• <b>Gaya Kekuatan (Power / Vibrasi Tinggi &gt; 200):</b> Menarik keajaiban, kesehatan penuh, dan rezeki yang mengalir lancar (peace/acceptance).</p>
            <p>Pilihlah jenis emosi dominan yang saat ini paling kuat mencengkeram dada atau pikiran Anda:</p>
        </div>
        """, unsafe_allow_html=True)
        
        emotion_choice = st.selectbox(
            "Pilih Emosi Dominan Anda & Lihat Kalibrasi Energinya:",
            [
                "Malu / Merasa Tidak Berharga (Kalibrasi: 20 Hz - Titik Terendah Batin)",
                "Bersalah / Menyesal / Menyalahkan Diri (Kalibrasi: 30 Hz - Merusak Imunitas Jiwa)",
                "Putus Asa / Hampa / Depresi (Kalibrasi: 50 Hz - Energi Beku)",
                "Sedih Mendalam / Kehilangan / Duka (Kalibrasi: 75 Hz - Kendi Hati Bocor)",
                "Takut / Cemas Cemas / Khawatir Berlebih (Kalibrasi: 100 Hz - Mempersempit Peluang)",
                "Marah / Dendam / Kecewa Berat (Kalibrasi: 150 Hz - Api yang Membakar Diri)",
                "Sombong / Egois / Gengsi Tinggi (Kalibrasi: 175 Hz - Ilusi Kekuatan)"
            ]
        )
        
        ancestral = st.radio(
            "Apakah pola rasa sakit atau hambatan ini juga dialami oleh orang tua atau leluhur Anda dahulu? (Pola Silsilah/Ancestral):",
            ["Ya, orang tua atau keluarga saya mengalami pola perjuangan emosi yang sama", "Tidak, ini hanya terjadi pada diri saya pribadi", "Saya tidak yakin, tetapi kemungkinan ada hubungannya"]
        )
        
        if st.button("Formulasikan Resep Terapi Paten Anda ➡️"):
            # Set Hawkins Calibration based on selection
            if "Malu" in emotion_choice:
                st.session_state.hawkins_score = 20
                st.session_state.emotional_feeling = "Malu (Rasa Tidak Berharga)"
            elif "Bersalah" in emotion_choice:
                st.session_state.hawkins_score = 30
                st.session_state.emotional_feeling = "Rasa Bersalah"
            elif "Putus Asa" in emotion_choice:
                st.session_state.hawkins_score = 50
                st.session_state.emotional_feeling = "Putus Asa & Hampa"
            elif "Sedih" in emotion_choice:
                st.session_state.hawkins_score = 75
                st.session_state.emotional_feeling = "Kesedihan Mendalam"
            elif "Takut" in emotion_choice:
                st.session_state.hawkins_score = 100
                st.session_state.emotional_feeling = "Ketakutan & Kecemasan"
            elif "Marah" in emotion_choice:
                st.session_state.hawkins_score = 150
                st.session_state.emotional_feeling = "Kemarahan & Dendam"
            else:
                st.session_state.hawkins_score = 175
                st.session_state.emotional_feeling = "Sombong & Gengsi"
                
            st.session_state.ancestral_bound = ancestral
            st.session_state.stage = "diagnosis_result"
            st.rerun()

    elif st.session_state.stage == "diagnosis_result":
        st.markdown("<h2>👑 Hasil Diagnosis & Resep Pemulihan Paten</h2>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class='luxury-card'>
            <span class='badge'>Laporan Kalibrasi Master Coach</span>
            <h3>Peta Sumbatan Energi Batin Anda:</h3>
            <p>• <b>Niche Hambatan:</b> {st.session_state.trauma_category}</p>
            <p>• <b>Sinyal Somatik (Tubuh):</b> {st.session_state.somatic_symptom}</p>
            <p>• <b>Emosi Dasar (Dr. Hawkins):</b> {st.session_state.emotional_feeling}</p>
            <p>• <b>Skor Kalibrasi Batin Anda:</b> <b style='color: #ef4444; font-size: 1.2rem;'>{st.session_state.hawkins_score} Hz (Force)</b></p>
            <p>• <b>Sumbatan Bawah Sadar (The Lie):</b> \"{st.session_state.limiting_belief}\"</p>
            <p>• <b>Ikatan Silsilah (Ancestral):</b> {st.session_state.ancestral_bound}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='coach-bubble'>
            <h3>"Resep Terapi Paten Anda Telah Siap."</h3>
            <p>Sistem batin Anda saat ini terkalibrasi di bawah level netral (200 Hz). Anda berada dalam mode <b>'Force'</b>, di mana tubuh mengunci amigdala otak untuk terus panik, tegang, dan menghalangi rezeki serta kebahagiaan masuk.</p>
            <p>Tugas kita adalah menaikkan getaran Anda melompati garis batas <b>Power (200 Hz+)</b> menuju level <b>Keikhlasan (Acceptance - 350 Hz)</b> dan <b>Kedamaian (Peace - 600 Hz)</b>.</p>
            <p><b>Silakan berpindah ke tab selanjutnya di atas secara berurutan:</b></p>
            <p>1. <b>💆‍♂️ Protokol SEFT Paten:</b> Untuk melonggarkan meridian saraf yang mengunci ketegangan fisik Anda secara instan.</p>
            <p>2. <b>🎵 Frekuensi Terapi:</b> Putar frekuensi murni 396 Hz atau 528 Hz untuk memprogram ulang getaran batin secara mendalam.</p>
            <p>3. <b>📝 Jurnal Deklaratif:</b> Lakukan penghancuran keyakinan palsu dan ritual pemutusan tali trauma keluarga terdahulu.</p>
        </div>
        """, unsafe_allow_html=True)
        
        diagnose_tts = (
            f"Hasil kalibrasi batin Anda menunjukkan skor energi sebesar {st.session_state.hawkins_score} hertz. "
            "Sistem saraf batin Anda saat ini mengunci energi trauma yang membuat tubuh berada dalam level Force yang menyiksa. "
            "Silakan ketuk tab Protokol SEFT Paten di atas untuk memulai sesi terapi batin sekarang juga."
        )
        text_to_speech_button(diagnose_tts, "🔊 Dengarkan Rekomendasi Terapi Master Coach")
        
        if st.button("Mulai Terapi Pemulihan Sekarang! 💆‍♂️"):
            st.info("Silakan ketuk tab **'💆‍♂️ Protokol SEFT Paten'** di bagian atas aplikasi Anda untuk memulai sesi terapi.")

# =============================================================================
# TAB 2: 💆‍♂️ PROTOKOL SEFT PATEN (INTERACTIVE GUIDE)
# =============================================================================
with tabs[1]:
    st.markdown("<h2>💆‍♂️ Protokol SEFT Paten Terbimbing</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8;'>Gabungan spiritualitas murni dan pengetukan meridian tubuh untuk merontokkan ketegangan trauma di tubuh Anda secara seketika.</p>", unsafe_allow_html=True)
    
    # Check if user has completed diagnostic
    if st.session_state.somatic_symptom == "":
        st.warning("⚠️ Anda belum melakukan Sesi Diagnostik batin. Silakan isi terlebih dahulu di tab '🤝 Sesi Coaching' agar Master Coach bisa mempersonalisasi teks terapi ini secara khusus untuk luka batin Anda.")
    
    # Interactive Step-by-step
    seft_steps = [
        {
            "title": "Langkah 1: Somatic Scan (Merasakan Hambatan)",
            "badge": "Somatic Scan",
            "desc": f"Pejamkan mata Anda sekarang. Rasakan area tubuh Anda yang mengalami ketegangan, yaitu: <b>{st.session_state.somatic_symptom if st.session_state.somatic_symptom else 'tubuh Anda'}</b>.<br><br>Hadirkan kembali emosi <b>{st.session_state.emotional_feeling if st.session_state.emotional_feeling else 'trauma Anda'}</b> dan kebohongan batin yang berbunyi: <i>\"{st.session_state.limiting_belief if st.session_state.limiting_belief else 'Saya tidak mampu/layak'}\"</i>.<br><br>Izinkan rasa sakit itu hadir seutuhnya di tubuh Anda tanpa penolakan. Bernapaslah dengan lembut.",
            "action": "Klik tombol di bawah jika Anda sudah bisa merasakan sensasinya dengan jelas.",
            "tts": f"Tutup mata Anda secara lembut. Rasakan dengan jujur sensasi tidak nyaman di {st.session_state.somatic_symptom if st.session_state.somatic_symptom else 'tubuh Anda'}. Katakan pada diri Anda sendiri: Saya mengizinkan rasa sakit ini hadir seutuhnya tanpa penolakan. Tarik napas panjang, embuskan."
        },
        {
            "title": "Langkah 2: Penyelarasan Pasrah & Menerima (The Setup)",
            "badge": "The Setup",
            "desc": f"Silangkan tangan Anda memeluk bahu Anda (posisi menyayangi diri sendiri) atau letakkan satu telapak tangan Anda tepat di area tubuh yang kaku (<b>{st.session_state.somatic_symptom if st.session_state.somatic_symptom else 'tubuh'}</b>).<br><br>Sambil memejamkan mata, ucapkan kalimat kepasrahan radikal ini sebanyak 3 kali dengan penuh penghayatan batin:<br><br><div class='prayer-container'>\"Ya Tuhan Semesta Alam... Meskipun tubuh saya merasakan <b>{st.session_state.somatic_symptom if st.session_state.somatic_symptom else 'ketegangan'}</b> akibat emosi <b>{st.session_state.emotional_feeling if st.session_state.emotional_feeling else 'trauma'}</b> yang selama ini menyumbat hidup saya, saya menerima luka ini sepenuhnya sebagai bagian dari perjalanan saya. Hari ini, saya izinkan seluruh saraf tubuh saya untuk rileks, dan saya pasrahkan kedamaian, kesembuhan, serta kelapangan batin saya seutuhnya hanya kepada-Mu.\"</div>",
            "action": "Ucapkan secara perlahan dan tulus dari lubuk hati terdalam, lalu klik tombol di bawah.",
            "tts": f"Ucapkan doa setup ini bersama saya dengan penuh kepasrahan: Ya Tuhan Semesta Alam... Meskipun tubuh saya merasakan {st.session_state.somatic_symptom if st.session_state.somatic_symptom else 'ketegangan'} akibat emosi {st.session_state.emotional_feeling if st.session_state.emotional_feeling else 'trauma'} yang selama ini menyumbat hidup saya, saya menerima luka ini sepenuhnya sebagai bagian dari perjalanan saya. Hari ini, saya izinkan seluruh saraf tubuh saya untuk rileks, dan saya pasrahkan kedamaian, kesembuhan, serta kelapangan batin saya seutuhnya hanya kepada-Mu. Tarik napas dalam, lepaskan."
        },
        {
            "title": "Langkah 3: Ketukan Ringan Meridian (The Tapping)",
            "badge": "The Tapping",
            "desc": "Gunakan dua ujung jari tangan dominan Anda untuk mengetuk dengan ringan, lembut, dan konstan (sekitar 5-7 kali ketukan) pada titik meridian berikut sembari membiarkan napas mengalir tenang dan mengulang kata emosi Anda (misal: <i>'rasa sakit ini... ketakutan ini... saya pasrah...'</i>):<br><br>1. <b>Ubun-ubun kepala</b> (Crown)<br>2. <b>Pangkal alis mata</b> (Eyebrow)<br>3. <b>Samping luar mata</b> (Side of eye)<br>4. <b>Tulang di bawah mata</b> (Under eye)<br>5. <b>Bawah hidung</b> (Under nose)<br>6. <b>Dagu</b> (Chin)<br>7. <b>Pertemuan tulang selangka</b> (Collarbone - <i>ketuk sedikit lebih lama</i>)<br>8. <b>Bawah ketiak</b> (Under arm)<br><br><i>Proses ini mengirimkan sinyal rasa aman biologis langsung ke amigdala otak Anda untuk merontokkan emosi negatif yang beku.</i>",
            "action": "Lakukan ketukan secara perlahan pada semua titik, lalu klik tombol di bawah.",
            "tts": "Gunakan dua ujung jari Anda untuk mengetuk secara ringan, lembut, dan perlahan di titik meridian Anda. Mulai dari ubun-ubun kepala, pangkal alis mata, samping luar mata, tulang di bawah mata, bawah hidung, dagu, pertemuan tulang selangka, dan bawah ketiak. Sembari mengetuk, bisikkan di dalam hati Anda: Saya terima rasa sakit ini, saya ikhlas, saya pasrahkan seutuhnya kepada-Mu."
        },
        {
            "title": "Langkah 4: Pelepasan & Penutupan (Selesai)",
            "badge": "The Release",
            "desc": f"Letakkan tangan Anda dengan rileks di atas pangkuan Anda. Tarik napas panjang yang sangat dalam dari dasar perut... tahan selama 3 detik... lalu embuskan secara perlahan melalui mulut secara melingkar dengan desahan lega: <b>\"Haaaa...\"</b>.<br><br><i>Rasakan ketegangan fisik di <b>{st.session_state.somatic_symptom if st.session_state.somatic_symptom else 'tubuh'}</b> Anda meleleh, larut, dan mengalir keluar bagaikan air. Seluruh beban batin dilepaskan seutuhnya ke alam semesta. Batin Anda kini lebih lapang, bersih, steril, dan tenang.</i>",
            "action": "Alhamdulillah, batin Anda telah melonggar. Anda bisa mengulangi terapi ini kapan saja ketegangan itu muncul kembali.",
            "tts": f"Letakkan tangan Anda di atas pangkuan secara rileks. Sekarang, tarik napas panjang yang sangat dalam dari dasar perut Anda... tahan sejenak... lalu embuskan secara perlahan melalui mulut dengan desahan lega yang panjang: haaaaaa... Sekali lagi, rasakan ketegangan di {st.session_state.somatic_symptom if st.session_state.somatic_symptom else 'tubuh'} Anda meleleh dan mengalir keluar bagaikan air. Alhamdulillah, batin Anda telah bersih dan tenang."
        }
    ]
    
    current_seft_step = st.session_state["seft_wizard_step"]
    
    # Render interactive wizard card
    st.markdown(f"""
    <div class='luxury-card'>
        <span class='badge'>{seft_steps[current_seft_step]['badge']}</span>
        <h3>{seft_steps[current_seft_step]['title']}</h3>
        <p style='color: #cbd5e1;'>{seft_steps[current_seft_step]['desc']}</p>
        <p style='color: #d4af37; font-weight: 600; margin-top: 15px;'>👉 {seft_steps[current_seft_step]['action']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Text to Speech Button for the Active Step
    text_to_speech_button(seft_steps[current_seft_step]['tts'], f"🔊 Panduan Suara: {seft_steps[current_seft_step]['badge']}")

    col1, col2 = st.columns(2)
    with col1:
        if current_seft_step > 0:
            if st.button("⬅️ Kembali"):
                st.session_state["seft_wizard_step"] -= 1
                st.rerun()
    with col2:
        if current_seft_step < 3:
            if st.button("Langkah Selanjutnya ➡️"):
                st.session_state["seft_wizard_step"] += 1
                st.rerun()
        else:
            if st.button("Ulangi Terapi Dari Awal 🔄"):
                st.session_state["seft_wizard_step"] = 0
                st.rerun()

# =============================================================================
# TAB 3: 🎵 FREKUENSI TERAPI (888 HZ, 528 HZ & 396 HZ HEALING AUDIO)
# =============================================================================
with tabs[2]:
    st.markdown("<h2>🎵 Terapi Frekuensi Suara Solfeggio</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8;'>Terapi gelombang audio bekerja secara ilmiah untuk mengembalikan sel tubuh dan saraf batin Anda yang rusak akibat trauma ke frekuensi harmonis.</p>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'>
        <h3>Pilih Frekuensi Penyembuhan Sesuai Luka Batin Anda:</h3>
        <p>Gunakan earphone Anda, carilah posisi duduk atau berbaring yang rileks, dan putar salah satu frekuensi di bawah ini selama terapi batin berlangsung:</p>
    </div>
    """, unsafe_allow_html=True)
    
    sound_option = st.selectbox(
        "Pilih Terapi Suara:",
        [
            "888 Hz - Meluruhkan Sumbatan Finansial & Mengaktifkan Aliran Rezeki",
            "528 Hz - Penyembuhan Trauma Seluler, Perbaikan DNA, & Transformasi Jiwa",
            "396 Hz - Melepaskan Rasa Bersalah, Malu, dan Rasa Takut yang Mendalam"
        ]
    )
    
    if "888 Hz" in sound_option:
        st.markdown("### 🎧 Putar Terapi Frekuensi Abundance 888 Hz:")
        st.video("https://www.youtube.com/watch?v=OGWZ9rsmsN4")
        st.info("💡 Frekuensi 888 Hz menyelaraskan vibrasi batin Anda agar selaras dengan getaran kemakmuran, membuka 'kendi bocor' keuangan, dan merelaksasi lambung/solar plexus.")
    elif "528 Hz" in sound_option:
        st.markdown("### 🎧 Putar Terapi Transformasi & Penyembuhan Trauma 528 Hz:")
        st.video("https://www.youtube.com/watch?v=vTPnwiCzAs8")
        st.info("💡 Frekuensi 528 Hz dikenal sebagai 'frekuensi cinta' atau mukjizat yang sangat efektif untuk merangsang penyembuhan emosional, meningkatkan energi vitalitas tubuh, dan memicu kedamaian mendalam.")
        st.markdown("""
        <div style='background-color: rgba(223, 177, 91, 0.1); border-left: 3px solid #dfb15b; padding: 12px; border-radius: 6px; margin-top: 10px; margin-bottom: 15px;'>
            📥 <b>Opsi Akses Offline & Unduh (Gratis & Legal):</b><br>
            • <a href='https://archive.org/download/SolTones/5%20%20Tansformation%20Miracles%20and%20DNA%20Repair%20528%20hz.mp3' target='_blank' style='color: #dfb15b; font-weight: bold;'>Unduh MP3 Nada Murni (Internet Archive)</a><br>
            • <a href='https://audio.com/aldo-ilardi/audio/meditative-528-hz-396-hz-390069' target='_blank' style='color: #dfb15b; font-weight: bold;'>Unduh Trek Meditasi Kombinasi (Audio.com)</a>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("### 🎧 Putar Terapi Pelepasan Ketakutan & Rasa Bersalah 396 Hz:")
        st.video("https://www.youtube.com/watch?v=LU_lEl-n5Ec")
        st.info("💡 Frekuensi 396 Hz dikalibrasi khusus untuk membersihkan trauma bawah sadar yang berupa rasa bersalah mendalam, ketakutan kronis, kecemasan masa depan, dan rasa minder/malu.")
        st.markdown("""
        <div style='background-color: rgba(223, 177, 91, 0.1); border-left: 3px solid #dfb15b; padding: 12px; border-radius: 6px; margin-top: 10px; margin-bottom: 15px;'>
            📥 <b>Opsi Akses Offline & Unduh (Gratis & Legal):</b><br>
            • <a href='https://archive.org/download/SolTones/3%20%20Freedom%20from%20Guilt%20and%20Fear%20396%20hz.mp3' target='_blank' style='color: #dfb15b; font-weight: bold;'>Unduh MP3 Nada Murni (Internet Archive)</a><br>
            • <a href='https://audio.com/reflexiones-solfeggio/audio/frecuencia-solfeggio-396-hz' target='_blank' style='color: #dfb15b; font-weight: bold;'>Unduh Nada Solfeggio Murni (Audio.com)</a>
        </div>
        """, unsafe_allow_html=True)

# =============================================================================
# TAB 4: 📝 JURNAL DEKLARATIF & CORD-CUTTING
# =============================================================================
with tabs[3]:
    st.markdown("<h2>📝 Jurnal Pelepasan & Pemutusan Tali Silsilah</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8;'>Pembersihan trauma tidak akan tuntas hanya dengan ditahan. Anda harus mengeluarkan 'Hutang Emosi' Anda ke media fisik secara radikal.</p>", unsafe_allow_html=True)
    
    therapy_mode = st.radio(
        "Pilih Terapi Pelepasan Anda Malam Ini:",
        ["✍️ Jurnal Terapeutik (Membantah Kebohongan Bawah Sadar)", "✂️ Ritual Pemutusan Tali Trauma Silsilah (Ancestral Cord-Cutting)"]
    )
    
    if "✍️" in therapy_mode:
        # Napoleon Hill Integration
        st.markdown("""
        <div class='luxury-card'>
            <h3>Langkah Pengosongan Kendi Pikiran (Metode Napoleon Hill):</h3>
            <p>Buku legendaris <b>Think and Grow Rich</b> mengajarkan kekuatan <i>Autosuggestion</i>. Batin Anda adalah magnet. Untuk mengubah realitas luar, Anda harus membakar kebohongan lama batin Anda dan menanamkan <i>Definite Chief Aim</i> (tujuan utama batin) dengan keyakinan spiritual mutlak.</p>
            <p>1. Tuliskan 'Kebohongan Lama' atau rasa takut Anda tentang luka batin tersebut di kolom pertama.</p>
            <p>2. Analisis mengapa keyakinan tersebut adalah kebohongan yang merusak hidup Anda.</p>
            <p>3. Tuliskan 'Deklarasi Kebenaran Baru' yang lapang untuk ditanam di pikiran bawah sadar Anda.</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("jurnal_trauma_healing_form_v3_form", clear_on_submit=True):
            lies_input = st.text_area(
                "Kebohongan lama / Rasa bersalah / Ketakutan Anda saat ini:",
                value=st.session_state.limiting_belief if st.session_state.limiting_belief else "",
                placeholder="Tuliskan semua unek-unek batin Anda tanpa ditahan..."
            )
            
            truth_input = st.text_area(
                "Deklarasi Kebenaran Berkelimpahan Baru (Definite Chief Aim Anda):",
                placeholder="Contoh: 'Saya layak untuk bahagia dan dicintai. Luka masa lalu tidak mendikte masa depan saya karena saya digenggam oleh Tuhan Semesta Alam yang Maha Pemurah.'"
            )
            
            submit_jurnal = st.form_submit_button("🔥 HANCURKAN KEBOHONGAN & INSTAL DATA BARU!")
            
            if submit_jurnal:
                if lies_input.strip() != "" and truth_input.strip() != "":
                    st.balloons()
                    st.success("✨ Alhamdulillah! Beban mental lama Anda telah terurai dan dilepaskan. Kebohongan batin Anda telah digantikan oleh data batin baru yang bercahaya dan berdaya tinggi!")
                else:
                    st.warning("Mohon isi kedua kolom batin di atas untuk menyempurnakan proses pemrograman ulang pikiran bawah sadar Anda.")
                    
    else:
        st.markdown("""
        <div class='luxury-card'>
            <h3>✂️ Ritual Visualisasi Pemutusan Tali Silsilah (Ancestral Cord-Cutting)</h3>
            <p>Sering kali trauma ketakutan, kegagalan berulang, kemiskinan, atau kemarahan kronis bukan berasal dari Anda pribadi, melainkan diwariskan dari perjuangan silsilah orang tua atau keluarga masa lalu.</p>
            <p><b>Cara Mempraktikkannya:</b></p>
            <ol>
                <li>Duduk tegak, pejamkan mata, dan bernapaslah dengan rileks.</li>
                <li>Bayangkan ada dua tali energi (cord) membentang dari belakang punggung Anda: tali kiri terhubung ke silsilah ibu, tali kanan terhubung ke silsilah ayah.</li>
                <li>Saksikan beban trauma atau kegagalan yang mereka bawa di masa lalu dengan rasa hormat dan kasih sayang.</li>
                <li>Visualisasikan seberkas cahaya emas hangat membungkus Anda dari langit, dan bayangkan sebuah <b>Kunci Emas (Golden Key)</b> memotong kedua tali warisan beban tersebut di belakang Anda secara aman dan penuh cinta kasih.</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### Deklarasikan Pelepasan Silsilah:")
        st.info("Letakkan tangan di dada Anda, tarik napas panjang, dan ucapkan kalimat ini secara lantang:")
        
        clearing_text = f"""
        \"Ibu, Ayah, terima kasih atas seluruh perjuangan hidup kalian yang berharga di masa lalu. Beberapa luka, ketakutan, kesempitan, dan kecemasan mungkin sempat mengalir ke dalam diri saya secara tidak sengaja.<br><br>
        Namun hari ini, dengan kesadaran penuh, saya memilih untuk melepaskan beban yang bukan milik saya ini. Apa yang tidak bisa kalian miliki di masa lalu, kini aman untuk saya terima dan wujudkan. Sifat trauma, luka batin, dan kelangkaan berhenti di saya.<br><br>
        Saya mengizinkan diri saya terbebas seutuhnya, hidup dalam kedamaian, kesehatan, dan kelimpahan, serta membagikan berkat indah ini kepada dunia.\"
        """
        st.markdown(f"<div class='prayer-container' style='font-size: 1.15rem !important;'>{clearing_text}</div>", unsafe_allow_html=True)
        
        # Add Voice TTS button for Ancestral Clearing
        ancestral_tts_text = (
            "Ibu, Ayah, terima kasih atas seluruh perjuangan hidup kalian yang berharga di masa lalu. "
            "Hari ini, dengan kesadaran penuh dan atas izin Tuhan Semesta Alam, saya memilih melepaskan beban yang bukan milik saya ini. "
            "Kelangkaan berhenti di saya. Masa depan saya adalah kedamaian dan kelimpahan."
        )
        text_to_speech_button(ancestral_tts_text, "🔊 Bimbingan Suara Ancestral Clearing (Meditatif)")

        if st.button("✂️ SAYA TELAH MEMOTONG TALI TRAUMA WARISAN SILSILAH!"):
            st.snow()
            st.success("✨ Selamat! Tali trauma kelangkaan dan luka masa lalu silsilah Anda telah diputus dengan penuh keikhlasan dan kedamaian batin. Energi kesembuhan kini mengalir bebas ke kehidupan Anda.")

# =============================================================================
# TAB 5: 📅 INDEKS PEMULIHAN & AGENDA HARIAN
# =============================================================================
with tabs[4]:
    st.markdown("<h2>📅 Agenda & Indeks Kesembuhan Harian</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8;'>Pemulihan trauma membutuhkan konsistensi harian (*Sincerity, Intensity, Consistency*) agar sistem saraf bawah sadar Anda benar-benar terkunci pada frekuensi keselamatan.</p>", unsafe_allow_html=True)
    
    # Session state for checklist progress
    if "trauma_pagi_1" not in st.session_state: st.session_state.trauma_pagi_1 = False
    if "trauma_pagi_2" not in st.session_state: st.session_state.trauma_pagi_2 = False
    if "trauma_siang_1" not in st.session_state: st.session_state.trauma_siang_1 = False
    if "trauma_siang_2" not in st.session_state: st.session_state.trauma_siang_2 = False
    if "trauma_malam_1" not in st.session_state: st.session_state.trauma_malam_1 = False
    if "trauma_malam_2" not in st.session_state: st.session_state.trauma_malam_2 = False

    # Alignment Score Calculation
    total_tasks = 6
    completed_tasks = sum([
        st.session_state.trauma_pagi_1,
        st.session_state.trauma_pagi_2,
        st.session_state.trauma_siang_1,
        st.session_state.trauma_siang_2,
        st.session_state.trauma_malam_1,
        st.session_state.trauma_malam_2
    ])
    progress_percentage = int((completed_tasks / total_tasks) * 100)

    # Progress visualizer
    st.markdown("<div class='luxury-card'>", unsafe_allow_html=True)
    st.markdown("<h3>📊 Indeks Pemulihan Batin Anda (Healing Progress Tracker)</h3>", unsafe_allow_html=True)
    st.progress(completed_tasks / total_tasks)
    
    if progress_percentage == 0:
        st.markdown(f"<p style='color: #94a3b8; font-weight: bold;'>Skor Keselarasan: {progress_percentage}% - Siap melakukan langkah awal pembersihan hari ini? ✨</p>", unsafe_allow_html=True)
    elif progress_percentage < 50:
        st.markdown(f"<p style='color: #d4af37; font-weight: bold;'>Skor Keselarasan: {progress_percentage}% - Sangat baik! Sistem batin Anda mulai terbiasa melepaskan ketegangan. 🌱</p>", unsafe_allow_html=True)
    elif progress_percentage < 100:
        st.markdown(f"<p style='color: #e2e8f0; font-weight: bold;'>Skor Keselarasan: {progress_percentage}% - Luar biasa! Wadah jiwa Anda sedang meluas untuk menampung ketenangan baru. 🌟</p>", unsafe_allow_html=True)
    else:
        st.balloons()
        st.markdown(f"<p style='color: #d4af37; font-weight: bold;'>Skor Keselarasan: 100% - Sempurna! Wadah keberlimpahan dan kesembuhan batin Anda sepenuhnya bersih, lapang, steril, dan bercahaya hari ini! 🔥🙏</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Interactive Checklist by Times
    st.markdown("### 🌅 Pagi Hari: Penyelarasan Jiwa & Syukur (15 Menit)")
    st.session_state.trauma_pagi_1 = st.checkbox(
        "📝 1. Jurnal Syukur & Menulis Komitmen (06.00 - 06.05)", 
        value=st.session_state.trauma_pagi_1,
        help="Tulis 3 hal yang Anda syukuri pagi ini untuk mengalihkan fokus dari trauma ke kelimpahan."
    )
    st.session_state.trauma_pagi_2 = st.checkbox(
        "🎧 2. Terapi Frekuensi Suara (06.05 - 06.15)", 
        value=st.session_state.trauma_pagi_2,
        help="Dengarkan frekuensi Solfeggio pilihan Anda selama 10 menit sambil rileks."
    )

    st.markdown("### ☀️ Siang Hari: Somatic Check & Relaksasi Saraf (5 Menit)")
    st.session_state.trauma_siang_1 = st.checkbox(
        "🧘‍♂️ 1. Pindai Ketegangan Tubuh & Gerakan Somatik (12.00 - 12.03)", 
        value=st.session_state.trauma_siang_1,
        help="Lakukan peregangan leher, bahu, dan napas lambung secara sadar."
    )
    st.session_state.trauma_siang_2 = st.checkbox(
        "💆‍♂️ 2. SEFT Tapping Kilat (12.03 - 12.05)", 
        value=st.session_state.trauma_siang_2,
        help="Lakukan tapping singkat 3 menit untuk membuang penat pekerjaan atau cemas emosi harian."
    )

    st.markdown("### 🌌 Malam Hari: Pelepasan Terapeutik & Reprogramming (20 Menit)")
    st.session_state.trauma_malam_1 = st.checkbox(
        "✍️ 1. Journaling Disproving the Lies (21.00 - 21.10)", 
        value=st.session_state.trauma_malam_1,
        help="Tulis ketakutan atau sumbatan emosional hari ini, bantai kebohongannya, instal kebenaran barunya."
    )
    st.session_state.trauma_malam_2 = st.checkbox(
        "😴 2. Pengantar Tidur Frekuensi Solfeggio (Sebelum Tidur)", 
        value=st.session_state.trauma_malam_2,
        help="Putar frekuensi Solfeggio pilihan Anda dengan volume sangat pelan menjelang tidur agar masuk ke pikiran bawah sadar."
    )

    if st.button("Mulai Agenda Hari Baru (Reset Indeks Tracker) 🔄"):
        st.session_state.trauma_pagi_1 = False
        st.session_state.trauma_pagi_2 = False
        st.session_state.trauma_siang_1 = False
        st.session_state.trauma_siang_2 = False
        st.session_state.trauma_malam_1 = False
        st.session_state.trauma_malam_2 = False
        st.rerun()

# Mobile usage footer
st.write("---")
st.markdown("<p style='text-align: center; font-size: 0.85rem !important; color: #64748b;'>Master Coach Trauma & Blockage Healing App V3<br>Dirancang secara eksklusif, elegan, dan profesional untuk kesejahteraan fisik, mental, dan spiritual dunia.<br>© 2026 Companion Abundance</p>", unsafe_allow_html=True)
