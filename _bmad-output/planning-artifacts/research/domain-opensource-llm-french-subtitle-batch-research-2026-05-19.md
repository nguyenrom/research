---
stepsCompleted: [1, 2, 3, 4, 5, 6]
inputDocuments: []
workflowType: 'research'
lastStep: 1
research_type: 'domain'
research_topic: 'Công cụ & quy trình opensource + LLM tạo phụ đề tự động cho video tiếng Pháp (.avi), xử lý hàng loạt, chạy local'
research_goals: 'Đánh giá độ chính xác/chất lượng nhận dạng tiếng Pháp (WER) và chất lượng phụ đề đầu ra; chạy local trên máy cá nhân (có/không GPU), ưu tiên opensource miễn phí; đầu ra phụ đề dịch sang tiếng Việt/Anh ở định dạng chuẩn .srt/.vtt'
user_name: 'Rom'
date: '2026-05-19'
web_research_enabled: true
source_verification: true
---

# Research Report: domain

**Date:** 2026-05-19
**Author:** Rom
**Research Type:** domain

---

## Research Overview

Nghiên cứu domain này khảo sát hệ sinh thái công cụ **opensource + LLM** để tự động tạo phụ đề cho video tiếng Pháp định dạng `.avi`, xử lý **hàng loạt**, **chạy local** trên máy cá nhân, với đầu ra dịch sang tiếng Việt/Anh ở định dạng chuẩn `.srt/.vtt`. Trọng tâm theo mục tiêu của Rom là **đánh giá độ chính xác/chất lượng** (WER tiếng Pháp) và tính khả thi local, ưu tiên miễn phí.

Kết luận cốt lõi: hệ sinh thái đã hội tụ quanh **Whisper-stack**; lựa chọn cân bằng nhất là pipeline `FFmpeg → WhisperX + fine-tune tiếng Pháp (bofenghuang/whisper-large-v3-french, WER ~4.8% FLEURS) → llm-subtrans + LLM local Qwen2.5 Apache-2.0 → người review`. NVIDIA Canary-1B-v2 / Parakeet-v3 là lựa chọn thay thế cho WER tiếng Pháp cao nhất hoặc batch quy mô lớn (cần GPU ≥16GB). Hai rào cản thương mại phải tránh: model dịch Meta (CC-BY-NC) và làm phụ đề video không có bản quyền.

Xem **Executive Summary** và bảng quyết định đầy đủ ở mục _Research Synthesis_ cuối tài liệu.

---

<!-- Content will be appended sequentially through research workflow steps -->

## Domain Research Scope Confirmation

**Research Topic:** Công cụ & quy trình opensource + LLM tạo phụ đề tự động cho video tiếng Pháp (.avi), xử lý hàng loạt, chạy local

**Research Goals:** Đánh giá độ chính xác/chất lượng nhận dạng tiếng Pháp (WER) và chất lượng phụ đề đầu ra; chạy local trên máy cá nhân (có/không GPU), ưu tiên opensource miễn phí; đầu ra phụ đề dịch sang tiếng Việt/Anh ở định dạng chuẩn .srt/.vtt

**Domain Research Scope:**

- Bối cảnh công nghệ ASR opensource — Whisper & biến thể, Vosk, NeMo, model mới; license, cộng đồng
- Benchmark độ chính xác tiếng Pháp — WER theo model size, ảnh hưởng chất lượng audio
- Kiến trúc pipeline batch — FFmpeg, VAD, alignment, yêu cầu phần cứng (CPU vs GPU/VRAM)
- Lớp LLM: dịch FR→VI/EN & hiệu đính — opensource vs API, giữ timing
- Công cụ tích hợp & hệ sinh thái — tool đóng gói sẵn, định dạng .srt/.vtt, license
- Đánh giá & rủi ro — phương pháp đo chất lượng, điểm yếu, khuyến nghị theo phần cứng

**Research Methodology:**

- All claims verified against current public sources (official repos, benchmark papers, project docs)
- Multi-source validation for critical domain claims
- Confidence level framework for uncertain information
- Comprehensive domain coverage with technical-domain-specific insights

**Scope Confirmed:** 2026-05-19

---

## Industry Analysis — Bối cảnh công nghệ ASR opensource + LLM cho phụ đề tiếng Pháp

> _Lưu ý dịch nghĩa: "thị trường" ở đây được hiểu là **hệ sinh thái công nghệ opensource** — đo bằng mức độ trưởng thành, độ phủ, tốc độ tiến hóa và độ chính xác, thay vì giá trị USD/CAGR._

### Market Size and Valuation — Quy mô & mức độ trưởng thành hệ sinh thái

Hệ sinh thái đã **hội tụ mạnh quanh Whisper** (OpenAI, MIT) làm model nền tảng cho mọi pipeline phụ đề chạy local. Quy mô cộng đồng (số sao GitHub, cập nhật 2026) phản ánh độ trưởng thành:

- _Lõi & engine_: openai/whisper ~99.7k★ (MIT, còn bảo trì 04/2026); whisper.cpp ~50k★ (MIT, rất active); faster-whisper ~23k★ (MIT, bảo trì 11/2025); WhisperX ~22k★ (BSD-2, bảo trì 04/2026).
- _Engine thay thế_: NVIDIA NeMo ~17k★ (Apache-2.0, rất active); Vosk ~14.7k★ (Apache-2.0, active 02/2026); SpeechBrain ~11.5k★.
- _Đã thực tế "chết"_: Coqui STT (~2.6k★, push cuối 03/2024) — **không nên dùng cho dự án mới**.
- _Tiếng Pháp_: là ngôn ngữ high-resource của Whisper; có fine-tune cộng đồng chất lượng cao (bofenghuang/whisper-large-v3-french).

_Total Market Size: Hệ sinh thái Whisper-based đã chiếm vị thế mặc định cho subtitling local; vài chục dự án vệ tinh trưởng thành._
_Growth Rate: Không có CAGR; tăng trưởng thể hiện qua nhịp ra model mới (large-v3 11/2023 → large-v3-turbo 10/2024 → NeMo Parakeet v3 / Canary v2 08/2025)._
_Market Segments: (1) Engine ASR, (2) lớp alignment/timestamp, (3) lớp LLM dịch & hiệu đính, (4) tool đóng gói GUI/CLI._
_Economic Impact: Đa số license MIT/Apache/BSD → dùng thương mại tự do; chi phí chủ yếu là phần cứng + nhân công review._
_Source: https://github.com/openai/whisper · https://github.com/SYSTRAN/faster-whisper · https://github.com/m-bain/whisperX · https://github.com/ggerganov/whisper.cpp · https://github.com/NVIDIA/NeMo · https://github.com/alphacep/vosk-api_

### Market Dynamics and Growth — Độ chính xác tiếng Pháp & động lực phát triển

Trọng tâm mục tiêu của Rom là **đánh giá độ chính xác**. WER (Word Error Rate, càng thấp càng tốt) cho tiếng Pháp — _phải đọc kỹ nhãn dataset_ (Common Voice = khó nhất, MLS = audiobook sạch nhất, FLEURS = trung bình, VoxPopuli = nhiễu/giọng vùng):

| Model (gốc OpenAI) | Common Voice 9 | MLS FR | VoxPopuli FR | FLEURS FR |
|---|---|---|---|---|
| whisper-small | 22.7 | 16.2 | 15.7 | 15.0 |
| whisper-medium | 16.0 | 8.9 | 12.2 | 8.7 |
| whisper-large-v2 | 13.9 | 7.3 | 11.4 | 8.3 |
| whisper-large-v3 | — | — | — | **6.59** (FLEURS, Open ASR Leaderboard) |
| large-v3-turbo | — | — | — | ~7.7 (1 benchmark độc lập, tin cậy trung bình) |

| Fine-tune tiếng Pháp (bofenghuang) | Common Voice | MLS FR | VoxPopuli | FLEURS FR |
|---|---|---|---|---|
| whisper-medium-french | 8.7 | 4.4 | 9.5 | 5.9 |
| whisper-large-v3-french | **7.28** | **3.98** | 8.91 | **4.84** |

_Growth Drivers: Model fine-tune tiếng Pháp giảm WER ~2 lần so với model gốc; "turbo"/distillation cho tốc độ cao gần như giữ nguyên độ chính xác; engine NeMo Canary 1B v2 (4.86% FLEURS FR) / Parakeet v3 (5.38%) đã **vượt Whisper large-v3 gốc** trên tiếng Pháp._
_Growth Barriers: tiny/base không dùng được cho tiếng Pháp (ước >30% WER); audio .avi nhiễu/bitrate thấp làm WER tăng +5→+25%; đa giọng +5→+10%._
_Cyclical Patterns: Nhịp release theo model nền tảng (OpenAI/NVIDIA), không theo mùa._
_Market Maturity: Whisper-stack đã chín; "turbo/distil" là pha tối ưu hiện tại (2024→2026)._
_Source: https://arxiv.org/html/2510.06961v3 · https://huggingface.co/bofenghuang/whisper-medium-french · https://huggingface.co/bofenghuang/whisper-large-v3-french · https://github.com/openai/whisper/discussions/1762_

### Market Structure and Segmentation — Cấu trúc & phân khúc công nghệ

_Primary Segments:_
1. **Engine ASR**: faster-whisper (CTranslate2, ~4× nhanh, MIT) — lựa chọn local tổng quát tốt nhất; whisper.cpp (C/C++, chạy tốt CPU & Apple Silicon, MIT); NeMo Parakeet/Canary (GPU, CC-BY-4.0).
2. **Lớp timestamp/alignment**: WhisperX (wav2vec2 forced alignment, BSD — timestamp khớp nhất cho phụ đề); whisper-timestamped (**AGPL-3.0** — copyleft, cẩn trọng); stable-ts.
3. **Lớp LLM dịch FR→VI/EN & hiệu đính**: MT opensource NLLB-200 / SeamlessM4T (**CC-BY-NC — chỉ phi thương mại**), OPUS-MT (CC-BY-4.0, thương mại OK), Argos/LibreTranslate (nhẹ, **đã bỏ gói tiếng Việt offline**, phải pivot qua tiếng Anh); LLM mở Qwen2.5/Gemma-SEA-LION/Llama mạnh nhất cho tiếng Việt.
4. **Tool đóng gói**: Subtitle Edit (GUI, GPL), Whisper-WebUI, subsai, Buzz (MIT), Vibe (offline + diarization), whisper-ctranslate2 (CLI, MIT).

_Sub-segment Analysis: Lớp dịch giữ timing tách riêng: llm-subtrans (MIT, GUI+CLI, đa LLM, active 04/2026), chatgpt-subtitle-translator, srt-llm-translator._
_Geographic Distribution: Cộng đồng toàn cầu; fine-tune tiếng Pháp tập trung ở HF (bofenghuang)._
_Vertical Integration: Pipeline điển hình: FFmpeg (.avi→WAV 16kHz mono) → VAD (Silero) → ASR (faster-whisper) → alignment (WhisperX) → cắt cue .srt/.vtt → LLM hiệu đính + dịch._
_Source: https://github.com/machinewrapped/llm-subtrans · https://huggingface.co/facebook/nllb-200-distilled-600M · https://github.com/Softcatala/whisper-ctranslate2 · https://github.com/thewh1teagle/vibe_

### Industry Trends and Evolution — Xu hướng & tiến hóa

_Emerging Trends:_ (1) "Turbo"/distillation thống trị 2024–2026 (large-v3-turbo, distil-whisper, Parakeet-TDT) — đổi chút độ chính xác lấy tốc độ/VRAM lớn; (2) NeMo Canary/Parakeet trở thành đối thủ Whisper đáng tin cho tiếng Pháp, license đã chuyển sang thương mại-friendly (CC-BY-4.0); (3) **LLM post-editing** (sửa dấu câu, chữ hoa, chính tả/dấu tiếng Pháp, sửa tên riêng — giảm tới ~30% WER trên named-entity) trở thành bước chuẩn bolt-on sau ASR.
_Historical Evolution: large-v2 → large-v3 (11/2023, giảm lỗi 10–20%) → large-v3-turbo (10/2024) → NeMo Parakeet v3 / Canary v2 (08/2025)._
_Technology Integration: LLM ngày càng được ghép vào cả hai đầu — hiệu đính transcript tiếng Pháp trước khi dịch, và dịch cue-by-cue giữ timestamp._
_Future Outlook: CPU-only ngày càng khả thi (whisper.cpp, faster-whisper int8); GPU vẫn cần cho large-v3 real-time + diarization._
_Source: https://huggingface.co/openai/whisper-large-v3-turbo · https://arxiv.org/pdf/2506.10779 · https://northflank.com/blog/best-open-source-speech-to-text-stt-model-in-2026-benchmarks_

### Competitive Dynamics — Động lực cạnh tranh

_Market Concentration: Tập trung cao quanh Whisper & các bản tái hiện (faster-whisper/whisper.cpp/WhisperX); NeMo là cực cạnh tranh thứ hai._
_Competitive Intensity: Cạnh tranh chủ yếu ở trục tốc độ/VRAM (turbo, quantization int8) và độ chính xác tiếng Pháp (fine-tune cộng đồng vs model gốc vs NeMo)._
_Barriers to Entry: Thấp về license (đa số MIT/Apache/BSD); rào cản thật là VRAM/phần cứng và công sức dựng pipeline batch._
_Innovation Pressure: Cao — chu kỳ ra model nền tảng ~6–12 tháng; lớp LLM tiến hóa nhanh hơn nữa._
_Điểm xung đột nguồn / độ tin cậy thấp:_ WER tiếng Pháp chính xác của large-v3-turbo (không có số chính thức); con số "Parakeet nhanh 10×" từ blog/vendor; tác động int8 lên WER tiếng Pháp chưa được đo trực tiếp; chất lượng FR→VI của NLLB/SeamlessM4T không có chrF/BLEU công bố riêng.
_Source: https://arxiv.org/html/2510.06961v3 · https://www.1qubit.de/en/ai/openai-whisper-performance-benchmarks · https://github.com/linto-ai/whisper-timestamped_

---

## Competitive Landscape — So sánh chi tiết công cụ cho use case `.avi` batch tiếng Pháp

### Key Players and Market Leaders — Các "ông lớn" & engine dẫn đầu

| Engine | Độ chính xác timestamp phụ đề | Tốc độ | VRAM | Dễ batch | Tiếng Pháp |
|---|---|---|---|---|---|
| **WhisperX** | Tốt nhất (forced-align cấp từ, có sẵn model align tiếng Pháp) | Nhanh (batched) | Trung bình | Mạnh (VAD batching) | Tốt |
| **faster-whisper** | Tốt (cấp segment; word-ts yếu hơn) | Nhanh | Thấp (int8) | Tốt | = Whisper large-v3 |
| **whisper.cpp** | = Whisper, timestamp thô hơn | CPU-friendly | Thấp nhất | Script được | = Whisper |
| **openai/whisper** | Chuẩn tham chiếu, drift trên audio dài | Chậm nhất | Cao nhất | Thủ công | Gold-standard đa ngữ |
| **NeMo Parakeet-TDT-0.6B-v3** | Word-ts tốt, ít kiểm chứng cho phụ đề | Nhanh nhất (RTFx ~3300) | Thấp | Script NeMo | "thắng tiếng Pháp dứt khoát" |
| **NeMo Canary-1B-v2** | Cao, ts qua NeMo | Chậm hơn Parakeet | Trung bình | Script NeMo | Vượt Whisper trên FR/ES/DE |

_Market Leaders: Whisper-stack (WhisperX / faster-whisper) là leader cho subtitling local — hệ sinh thái forced-alignment & tooling trưởng thành nhất._
_Major Competitors: NVIDIA NeMo (Canary-1B-v2 là đối thủ độ chính xác tiếng Pháp; Parakeet-v3 là đối thủ tốc độ)._
_Emerging Players: Parakeet-TDT-0.6B-v3 / Canary-1b-v2 (09/2025) — entrant đáng chú ý nhất 2025–2026._
_Global vs Regional: Cộng đồng toàn cầu; model align tiếng Pháp & fine-tune FR tập trung trên Hugging Face._
_Source: https://modal.com/blog/choosing-whisper-variants · https://northflank.com/blog/best-open-source-speech-to-text-stt-model-in-2026-benchmarks · https://whispernotes.app/blog/parakeet-v3-default-mac-model_

### Market Share and Competitive Positioning — Định vị

- **WhisperX (backend large-v3)** thắng về **độ chính xác timestamp phụ đề + batch + tiếng Pháp** (ship sẵn model wav2vec2 align FR). _Cảnh báo:_ từ chứa chữ số ("2014", "€13") bị timestamp sai/thiếu — đáng lưu ý với số tiếng Pháp (issue #1298, #1247).
- **faster-whisper** thắng về **batch ít ma sát nhất + VRAM thấp nhất**.
- **NeMo Canary-1B-v2** là **lựa chọn tối ưu nếu WER tiếng Pháp là ưu tiên số 1** (vượt Whisper large-v3 gốc trên FR), đổi lại chi phí chuyển đổi sang NeMo cao.

_Competitive Positioning: WhisperX = "chính xác timestamp"; faster-whisper = "mặc định an toàn, nhẹ"; NeMo = "độ chính xác FR cao nhất"; whisper.cpp = "CPU/offline tối giản"._
_Value Proposition Mapping: Trục cạnh tranh chính = (1) độ chính xác timestamp phụ đề, (2) WER tiếng Pháp, (3) tốc độ/VRAM._
_Customer Segments Served: Dev cần pipeline tùy biến (WhisperX/faster-whisper) vs người dùng cuối cần GUI (Subtitle Edit/Buzz/Vibe)._
_Source: https://modal.com/blog/choosing-whisper-variants · https://github.com/m-bain/whisperX/issues/1298 · https://medium.com/@unicornporated/subtitle-engineering-showdown-of-speech-to-text-giants-and-building-the-ultimate-subtitle-24ea2c21c6bf_

### Competitive Strategies and Differentiation — Công cụ đóng gói (batch + dịch)

- **Subtitle Edit** — _winner cho batch + hậu kỳ + đa định dạng_. Có nút **Batch mode**, khuyến nghị bundle Purfview Faster-Whisper, auto-translate qua Google/DeepL **và** LLM/ChatGPT/Ollama. Được cộng đồng đề xuất nhất quán nhất cho workflow batch+dịch trọn gói.
- **Buzz** — UI batch đơn giản nhất (hàng đợi nhiều file, whisper.cpp/OpenAI), nhẹ, biên tập yếu hơn.
- **Vibe** — tương đương Buzz, 90+ ngôn ngữ, diarization, export .srt, offline hoàn toàn.
- **subsai** — batch qua file danh sách path + có sẵn tùy chọn model/nguồn/đích dịch.
- **whisper-ctranslate2** — CLI batched VAD (2–4×) nhưng task "translate" **chỉ ra tiếng Anh** → không dùng được cho tiếng Việt.

_Cost Leadership: whisper.cpp / faster-whisper int8 (rẻ phần cứng, CPU-OK)._
_Differentiation: WhisperX (alignment), Subtitle Edit (GUI trọn gói)._
_Focus/Niche: subsai/Buzz/Vibe (người dùng cuối, offline đơn giản)._
_Innovation Approaches: turbo/distillation (tốc độ), forced-alignment (độ chính xác timestamp), LLM bolt-on (hậu kỳ + dịch)._
_Source: https://an4t.com/subtitle-edit-whisper-vosk-auto-subtitles-guide/ · https://subtitleedit.net/subtitle-edit-whisper/ · https://nlsblog.org/2025/12/17/lab-notes-transcription-with-vibe-and-buzz/ · https://github.com/absadiki/subsai · https://github.com/Softcatala/whisper-ctranslate2_

### Business Models and Value Propositions — Lớp dịch LLM (đối đầu)

- **llm-subtrans** (machinewrapped) — active, 8 provider gồm **LLM local qua LM Studio/OpenAI-compatible**, batch theo cảnh giữ style/vị trí, chuẩn hóa dòng dài. _Tự README cảnh báo:_ "không nên kỳ vọng kết quả tốt từ model local".
- **chatgpt-subtitle-translator** (Cerlancism) — thêm "structured mode" (10/2025) đồng bộ timing, format TOON gọn token, có thể gộp cue.
- **Subtitle Edit auto-translate** — tích hợp nhất nhưng LLM mode mới, kém context-aware hơn tool chuyên dụng.
- **Tự dựng LLM local** — riêng tư/chi phí tối ưu nhất, giữ timing dễ (chỉ dịch trường text), nhưng tự xử lý batch + giãn độ dài tiếng Việt.

_Primary Business Models: 100% opensource miễn phí; "doanh thu" = tiết kiệm chi phí + chủ quyền dữ liệu._
_Revenue Streams: Không có (FOSS); chi phí ẩn = token API nếu dùng LLM cloud, hoặc GPU nếu LLM local._
_Customer Relationship: Giữ timestamp gần như đã là bài toán giải xong (chỉ dịch trường text); khác biệt thật = context-batching cho mạch lạc + xử lý **giãn độ dài tiếng Việt** (llm-subtrans làm rõ điểm này)._
_Source: https://github.com/machinewrapped/llm-subtrans · https://github.com/Cerlancism/chatgpt-subtitle-translator_

### Competitive Dynamics and Entry Barriers — Rào cản & chi phí chuyển đổi

_Barriers to Entry: License thấp (đa số MIT/Apache/BSD); rào cản thật = VRAM/phần cứng + công sức dựng pipeline._
_Switching Costs: **Lock-in Whisper thấp-trung bình** — cùng bộ trọng số large-v3 dùng lại qua openai-whisper / faster-whisper (CTranslate2) / whisper.cpp (GGUF) / WhisperX, đổi runtime ≈ re-convert, gần như không đổi chất lượng. **Lock-in định dạng** mới là chi phí thật: CTranslate2 vs GGUF vs HF vs NeMo `.nemo` — **NeMo khó "thoát" nhất** (kiến trúc khác, phải re-tooling toàn bộ)._
_Market Consolidation: Không M&A (FOSS); "hợp nhất" thể hiện qua việc cộng đồng hội tụ về Whisper-stack._
_Switching Costs (artifact): Đầu ra .srt/.vtt là chuẩn phổ quát → **zero lock-in ở tầng sản phẩm**; chiến lược an toàn = giữ engine ASR thay thế được sau một interface .srt ổn định._
_Source: https://github.com/SYSTRAN/faster-whisper · https://arxiv.org/pdf/2509.14128_

### Ecosystem and Partnership Analysis — Hệ sinh thái

_Supplier Relationships: Phụ thuộc model nền từ OpenAI (Whisper) & NVIDIA (NeMo); model align từ HF (wav2vec2, bofenghuang fine-tune FR)._
_Distribution Channels: GitHub + Hugging Face + PyPI; tool GUI qua release nhị phân (Subtitle Edit, Buzz, Vibe)._
_Technology Partnerships: WhisperX = faster-whisper + wav2vec2 + pyannote (diarization, cần HF token); Subtitle Edit ↔ Purfview Faster-Whisper._
_Ecosystem Control: OpenAI/NVIDIA kiểm soát tầng model nền; cộng đồng kiểm soát tầng runtime/tooling/dịch — đây là điểm tạo tính cạnh tranh & tránh lock-in._
_Điểm tin cậy thấp / xung đột nguồn: Xếp hạng "tốt nhất cho phụ đề" và verdict tool dịch là ý kiến thực hành (không phải benchmark độc lập); chưa có nguồn nào benchmark tất cả engine trên độ chính xác timestamp phụ đề tiếng Pháp cụ thể._
_Source: https://modal.com/blog/open-source-stt · https://github.com/m-bain/whisperX_

---

## Regulatory Requirements — Tuân thủ license, quyền riêng tư & bản quyền

> _Đây là tổng hợp tham khảo, **không phải tư vấn pháp lý**. Sự thật pháp lý có trích dẫn; phần diễn giải đánh dấu [DIỄN GIẢI] hoặc [TIN CẬY THẤP]. Kiểm tra với luật sư trước khi triển khai thương mại._

### Applicable Regulations — Quy định áp dụng

- **License phần mềm/model** (xem chi tiết mục Licensing): MIT/Apache/BSD an toàn thương mại; AGPL-3.0 rủi ro nếu thành dịch vụ mạng; CC-BY-NC **cấm dùng thương mại**.
- **GDPR** (EU 2018): xử lý ghi âm giọng nói tiếng Pháp = xử lý dữ liệu cá nhân.
- **EU AI Act** (2024): nghĩa vụ minh bạch Điều 50(2) cho nội dung do AI tạo — hiệu lực **02/08/2026**.
- **Luật bản quyền** (US/EU): phụ đề là tác phẩm phái sinh của video gốc.

_Source: https://creativecommons.org/licenses/by-nc/4.0/legalcode.en · https://artificialintelligenceact.eu/article/50/ · https://www.copyright.gov/circs/circ14.pdf_

### Industry Standards and Best Practices — Chuẩn thực hành

- Giữ engine ASR thay thế được sau interface `.srt/.vtt` ổn định (tránh lock-in định dạng).
- Lưu giữ file LICENSE/NOTICE của mọi thành phần FOSS dùng trong pipeline.
- Gắn nhãn "Phụ đề do AI tạo / dịch máy" trên sản phẩm giao (chuẩn bị cho AI Act).
- Xử lý audio **local/offline** làm kiến trúc mặc định để giảm phơi nhiễm GDPR.

_Source: https://artificialintelligenceact.eu/transparency-rules-article-50/_

### Compliance Frameworks — Khung tuân thủ license (trọng tâm)

| License | Thành phần | Nghĩa vụ / rủi ro thương mại |
|---|---|---|
| **MIT/BSD** | openai-whisper (cả **trọng số** model), faster-whisper, whisper.cpp, WhisperX | An toàn thương mại; chỉ cần giữ thông báo bản quyền + license khi **phân phối lại** code. Dùng nội bộ gần như không nghĩa vụ. |
| **AGPL-3.0** | `whisper-timestamped` (+ phụ thuộc `dtw-python` GPL-v3) | [DIỄN GIẢI] Tool batch CLI **nội bộ** không kích hoạt §13; nhưng nếu thành **dịch vụ mạng/SaaS** phải mở toàn bộ source cho người dùng từ xa → "AGPL contamination". Thay bằng word-timestamp của WhisperX/faster-whisper cho sản phẩm phân phối. |
| **CC-BY-NC 4.0** | Meta NLLB-200, SeamlessM4T, MMS | Test là **bản chất việc dùng, không phải người dùng**. [DIỄN GIẢI, tin cậy cao] Dịch vụ dịch **có thu phí** = dùng thương mại → **vi phạm**. Không dùng cho luồng tạo doanh thu. |
| **CC-BY-4.0** | NVIDIA Parakeet v3 / Canary v2 | Thương mại OK; **bắt buộc ghi công** (tên NVIDIA + tên model + link license + nêu nếu đã sửa). |
| **Llama 3.x Community** | LLM dịch | Thương mại OK royalty-free; điều khoản >700M MAU (không liên quan ở quy mô nhỏ); AUP + ghi công "Built with Llama" khi phân phối. Không phải OSI open-source. |
| **Qwen2.5** | LLM dịch | Phần lớn size (0.5/1.5/7/14/32B) **Apache-2.0** an toàn; **3B & 72B dùng license Qwen riêng**. Dùng size Apache-2.0 để tránh ràng buộc. |
| **Gemma** | LLM dịch | Thương mại OK nhưng phải truyền tiếp use-restriction + kèm notice khi phân phối. |

_Source: https://github.com/linto-ai/whisper-timestamped/issues/215 · https://wiki.creativecommons.org/wiki/4.0/NonCommercial · https://www.llama.com/llama3_1/license/ · https://huggingface.co/Qwen/Qwen2.5-72B-Instruct/blob/main/LICENSE · https://ai.google.dev/gemma/terms_

### Data Protection and Privacy — GDPR

Phiên âm giọng nói tiếng Pháp đã ghi = **xử lý dữ liệu cá nhân**; trở thành **dữ liệu sinh trắc đặc biệt (Điều 9)** chỉ khi xử lý để nhận dạng duy nhất một người (ví dụ diarization/voiceprint). [DIỄN GIẢI] Chạy ASR + LLM **hoàn toàn local/offline giảm mạnh phơi nhiễm GDPR**: không chuyển cho bên thứ ba → không cần thỏa thuận xử lý (Điều 28), không cần cơ chế chuyển dữ liệu quốc tế (Điều 44–49). Gửi audio/phụ đề tới **API LLM cloud** (OpenAI/Anthropic/Google) biến nhà cung cấp thành processor → cần DPA, cơ sở pháp lý, và cơ chế chuyển (SCCs / EU-US DPF). **Local là kiến trúc ưu tiên về quyền riêng tư.**

_Source: https://www.aepd.es/en/press-and-communication/blog/ai-voice-transcription_

### Licensing and Certification — EU AI Act

ASR/dịch máy **không thuộc nhóm rủi ro cao** (Annex III) — thường là **rủi ro hạn chế**. Nghĩa vụ liên quan = **Điều 50(2) minh bạch**: nội dung audio/text tổng hợp do AI tạo phải được đánh dấu; bên triển khai phải công bố là do AI tạo/dịch. [DIỄN GIẢI] Phụ đề do AI tạo/dịch nhiều khả năng thuộc phạm vi → giảm thiểu bằng nhãn "Phụ đề do AI tạo / dịch máy". **Hiệu lực Điều 50: 02/08/2026.**

_Source: https://artificialintelligenceact.eu/article/50/ · https://artificialintelligenceact.eu/transparency-rules-article-50/_

### Implementation Considerations — Bản quyền & cân nhắc thực thi

- **Video nguồn**: phim/video là tác phẩm được bảo hộ; làm phụ đề (phiên âm + dịch thoại) là **tác phẩm phái sinh**. Làm phụ đề cho video bên thứ ba **không có phép = vi phạm**. → Chỉ xử lý nội dung mình sở hữu/được cấp phép/hết hạn bản quyền; lấy cam kết quyền + bồi hoàn từ khách hàng.
- **Đầu ra AI**: bản phiên âm/dịch máy thô **nhiều khả năng không được bảo hộ bản quyền độc lập** (US Copyright Office, 01/2025 — cần đóng góp sáng tạo của con người). Thêm bước biên tập/QA của người để tạo lớp bảo hộ mỏng; quy định IP với khách hàng bằng hợp đồng.

_Source: https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf · https://www.copyright.gov/circs/circ14.pdf_

### Risk Assessment — Bảng đánh giá rủi ro

| Lĩnh vực | Vấn đề | Mức độ | Giảm thiểu |
|---|---|---|---|
| License | NLLB/SeamlessM4T/MMS (CC-BY-NC) trong dịch vụ **thu phí** | **Cao** | Không dùng thương mại; chuyển dịch sang Qwen2.5 Apache-2.0 / Llama (kèm ghi công) / MT có license |
| License | `whisper-timestamped` AGPL trong sản phẩm SaaS/phân phối | **Cao** | Nội bộ thì OK; với SaaS dùng word-timestamp của WhisperX/faster-whisper |
| License | Qwen2.5 3B/72B hoặc Gemma license tùy chỉnh | Trung bình | Dùng size Qwen Apache-2.0; tuân thủ notice/pass-through nếu dùng Gemma |
| License | Ghi công MIT/BSD khi phân phối lại | Thấp | Giữ file LICENSE/NOTICE |
| Quyền riêng tư | Giọng nói tiếng Pháp = dữ liệu cá nhân (có thể đặc biệt) | Trung bình | Xử lý **local/offline**; tránh API LLM cloud, hoặc ký DPA + SCCs; ghi nhận cơ sở pháp lý |
| AI Act | Minh bạch Điều 50(2), hiệu lực 02/08/2026 | Thấp–Trung bình | Gắn nhãn "Phụ đề do AI tạo / dịch máy" |
| Bản quyền | Làm phụ đề video bên thứ ba không có quyền | **Cao** | Chỉ xử lý video sở hữu/được cấp phép/public-domain; lấy cam kết quyền + bồi hoàn |
| Bản quyền | Bảo hộ mỏng/không có trên đầu ra AI | Thấp | Thêm biên tập/QA của người; chốt điều khoản IP bằng hợp đồng |

**Chốt:** Hai rào cản thương mại lớn nhất = (1) model dịch Meta CC-BY-NC và (2) làm phụ đề video bên thứ ba không có quyền; thành phần AGPL an toàn khi nội bộ nhưng "độc" với sản phẩm phân phối/SaaS. Xử lý local-only giảm mạnh rủi ro GDPR.

---

## Technical Trends and Innovation — Xu hướng kỹ thuật 2025–2026

### Emerging Technologies — Model ASR thế hệ mới (đều hỗ trợ tiếng Pháp)

Chuyển dịch lớn nhất: **Whisper không còn là mặc định** — các model encoder đa ngữ-native nhanh hơn đang vượt lên, hầu hết hỗ trợ tiếng Pháp rõ ràng.

- **NVIDIA Parakeet-TDT-0.6B-v3 / Canary-1B-v2** (09/2025): 25 ngôn ngữ gồm FR, dataset Granary 1.7M giờ. Canary-1B-v2 đứng đầu leaderboard độ chính xác đa ngữ HF; Parakeet-v3 throughput cao nhất (~25–30× Whisper trên GPU datacenter), cho ASR FR + dịch nói trong 1 model. _Đã benchmark, không phải hype._
- **Whisper large-v3-turbo**: nay là baseline thực tế (809M params, ~6× nhanh, lệch WER 1–2% so large-v3, 99+ ngôn ngữ, ~6GB VRAM) — mạnh nhất về **độ phủ ngôn ngữ** nhưng không còn dẫn đầu tốc độ/độ chính xác.
- **Kyutai STT `stt-1b-en_fr`** (06/2025): chuyên **Pháp + Anh**, streaming, **word-level timestamp + semantic VAD tích hợp sẵn**, trọng số CC-BY-4.0 — release streaming liên quan tiếng Pháp nhất.
- **IBM Granite Speech 3.3** (05/2025): ASR+AST 2 pass, tinh chỉnh cho FR.
- **distil-whisper** (distil-large-v3): vẫn dùng được nhưng bị Parakeet/turbo vượt cho batch.

_Source: https://arxiv.org/abs/2509.14128 · https://blogs.nvidia.com/blog/speech-ai-dataset-models/ · https://kyutai.org/stt · https://huggingface.co/ibm-granite/granite-speech-3.3-8b_

### Digital Transformation — Model LLM-native / đa phương thức (audio → text đã dịch)

End-to-end "1 model: audio → phụ đề đã dịch" nay **khả thi opensource thật**, nhưng có 1 lưu ý then chốt cho phụ đề.

- **Mistral Voxtral** (07/2025, lab Pháp, trọng số Apache): Voxtral Small (24B) vượt Gemini 2.5 Flash & GPT-4o-mini Audio trên dịch nói EN↔FR; Mini (4.7B) cho edge.
- **Voxtral Transcribe 2** (02/2026): ~4% WER trên FLEURS, hỗ trợ FR rõ, **timestamp start/end theo từng từ**, ~4B params chạy on-device — tín hiệu đầu tiên thu hẹp khoảng trống "model end-to-end thiếu timestamp".
- **SeamlessM4T-v2** (~100 ngôn ngữ, FR↔VI trực tiếp — nhưng CC-BY-NC), **Qwen2.5-Omni** (audio/video-in, streaming).

_Tradeoff (thực tế đã benchmark):_ model AST end-to-end cho text dịch trôi chảy nhưng **trước đây thiếu word-timestamp tin cậy** — tử huyệt cho timing phụ đề. Pipeline cổ điển **ASR → forced-align → LLM dịch** vẫn thắng về độ chính xác timestamp. Voxtral Transcribe 2 là tín hiệu khoảng trống đang đóng lại, _nhưng độ chính xác timestamp FR chưa được benchmark độc lập → đầy hứa hẹn, chưa được kiểm chứng._

_Source: https://slator.com/mistral-debuts-open-source-voxtral-ai-speech-translation-transcription/ · https://venturebeat.com/technology/mistral-drops-voxtral-transcribe-2-an-open-source-speech-model-that-runs-on · https://huggingface.co/docs/transformers/model_doc/seamless_m4t_v2_

### Innovation Patterns — Tối ưu hiệu năng & hậu kỳ LLM

_Hiệu năng:_ CTranslate2/faster-whisper (~4× + batched 2–4× nữa, int8/int4, hỗ trợ AMD ROCm); **vLLM** thành lựa chọn ưu tiên cho LLM dịch self-host (continuous batching, prefix KV-cache); diarization: **pyannote 3.1** (nhẹ, DER ~11–19%, lựa chọn local thực tế) vs NVIDIA Sortformer (chính xác hơn nhưng nặng GPU); WhisperX vẫn là pipeline ASR+align+diarize chuẩn cho batch.

_Hậu kỳ LLM:_ (1) **dịch đa-pass dạng agentic** (sinh → tự phản tỉnh → soát adequacy → tinh chỉnh fluency) đo được chất lượng cao hơn one-pass; (2) huấn luyện LLM riêng cho phụ đề (ALPO, 2026); (3) **Quality Estimation reference-free** chọn ví dụ in-context; (4) MT theo ngữ cảnh tài liệu (document-level) nay là chuẩn cho mạch lạc phụ đề.

_Source: https://github.com/OpenNMT/CTranslate2 · https://arxiv.org/pdf/2505.01560 · https://arxiv.org/html/2602.01068v1 · https://arxiv.org/pdf/2406.07970_

### Future Outlook — Triển vọng 2026+

Hội tụ về **một model đa phương thức xuất phụ đề đã dịch kèm timestamp** (Voxtral Transcribe 2 là tín hiệu dẫn đầu), cộng một lớp LLM agentic mỏng để chuẩn hóa tốc độ đọc/timing & thuật ngữ. Model lớp 4B chạy on-device làm pipeline FR full-local khả thi. _Khoảng trống còn lại:_ độ chính xác **word-timestamp FR** của model end-to-end chưa được kiểm chứng độc lập; **FR→Việt là cặp low-resource** — đa số benchmark AST xoay quanh X↔Anh, chất lượng FR→VI trực tiếp gần như chưa được kiểm thử ở model mở.

_Source: https://venturebeat.com/technology/mistral-drops-voxtral-transcribe-2-an-open-source-speech-model-that-runs-on · https://northflank.com/blog/best-open-source-speech-to-text-stt-model-in-2026-benchmarks_

### Implementation Opportunities — Cơ hội triển khai (local batch FR→VI/EN)

- **Stack khuyến nghị:** Parakeet-TDT-0.6B-v3 _hoặc_ faster-whisper large-v3-turbo (ASR FR + word-timestamp qua WhisperX/CTranslate2 batched) → dịch LLM đa-pass agentic (FR→VI/EN) qua vLLM local → pass QE + chuẩn hóa tốc độ đọc.
- **Pivot FR→EN→VI** qua trung gian tiếng Anh có thể tốt hơn FR→VI trực tiếp do khoảng trống low-resource (cần kiểm chứng thực nghiệm trên dữ liệu của bạn).
- Kyutai `stt-1b-en_fr` và Voxtral Mini (4B, Apache, on-device) cho pipeline FR offline hoàn toàn.
- Quantization int8/int4 + batched inference → throughput 8–16× trên GPU local khiêm tốn.

_Source: https://github.com/SYSTRAN/faster-whisper · https://github.com/m-bain/whisperX_

### Challenges and Risks — Thách thức & rủi ro

- **Độ chính xác timestamp FR** của model AST end-to-end chưa được kiểm chứng cho đồng bộ phụ đề → giữ ASR→align→dịch làm mặc định đáng tin.
- **FR→VI low-resource**: benchmark mở xoay quanh tiếng Anh; chất lượng FR→VI dao động, cần người/QE thẩm định.
- Sortformer/Canary-1B cần ≥16GB VRAM; pyannote 3.1 + Parakeet/turbo là dấu chân local thực tế.
- Số WER nhà cung cấp tự công bố (Voxtral "~4% FLEURS", Parakeet "10× nhanh") chỉ mang tính định hướng cho tới khi có benchmark FR bên thứ ba.

_Source: https://vast.ai/article/whisper-pyannote-sortformer-diarization-vast · https://arxiv.org/abs/2509.14128_

## Recommendations — Khuyến nghị

### Technology Adoption Strategy — Chiến lược chọn công nghệ

**Phương án A (Khuyến nghị — cân bằng chất lượng/độ chính xác, an toàn license):**
`FFmpeg` (.avi → WAV 16kHz mono) → **WhisperX** với backend **faster-whisper large-v3** _hoặc_ fine-tune **`bofenghuang/whisper-large-v3-french`** (WER FR ~4.8% FLEURS) → cắt cue `.srt/.vtt` → **llm-subtrans + LLM local Qwen2.5 size Apache-2.0** dịch FR→VI/EN (giữ timing) → người review.
- _Vì sao:_ độ chính xác timestamp tốt nhất + WER FR thấp nhất + toàn bộ MIT/BSD/Apache (an toàn thương mại) + chạy local (giảm rủi ro GDPR).

**Phương án B (Tối đa WER tiếng Pháp / tốc độ batch lớn):**
Thay engine ASR bằng **NVIDIA Canary-1B-v2** (độ chính xác FR cao nhất, CC-BY-4.0 — nhớ ghi công) hoặc **Parakeet-TDT-0.6B-v3** (throughput cao nhất cho batch hàng trăm video). Phần còn lại như PA A.
- _Đánh đổi:_ chi phí "thoát" khỏi NeMo cao hơn (định dạng `.nemo`), cần GPU ≥16GB cho Canary.

### Innovation Roadmap — Lộ trình

1. **Ngắn hạn (làm ngay):** dựng PA A; benchmark thử trên ~5–10 video `.avi` thật của bạn, đo WER thủ công + kiểm tra timing số/chữ số (lỗi đã biết của WhisperX).
2. **Trung hạn:** thử pivot FR→EN→VI vs FR→VI trực tiếp, chọn nhánh cho chất lượng tiếng Việt tốt hơn; thêm pass QE + chuẩn hóa tốc độ đọc.
3. **Theo dõi:** Voxtral Transcribe 2 (one-model audio→phụ đề dịch kèm timestamp) — đánh giá lại khi có benchmark FR timestamp độc lập.

### Risk Mitigation — Giảm thiểu rủi ro

- **License:** tránh NLLB/SeamlessM4T/MMS (CC-BY-NC) & `whisper-timestamped` (AGPL) nếu thương mại/SaaS; dùng Qwen2.5 Apache-2.0.
- **Bản quyền:** chỉ xử lý video sở hữu/được cấp phép; lấy cam kết quyền từ khách hàng.
- **Chất lượng:** luôn có vòng người review (WER tăng +10–25% với audio `.avi` nhiễu/đa giọng); không giao thẳng đầu ra AI thô.
- **GDPR/AI Act:** giữ pipeline local; gắn nhãn "Phụ đề do AI tạo / dịch máy" (chuẩn bị Điều 50, 02/08/2026).

---

# Phụ đề tiếng Pháp tự động bằng Opensource + LLM: Tổng hợp nghiên cứu domain

## Executive Summary

Năm 2026, việc tạo phụ đề tiếng Pháp tự động chạy **hoàn toàn local, miễn phí, chất lượng cao** đã là hiện thực kỹ thuật — không còn phải đánh đổi giữa "miễn phí" và "đủ tốt". Hệ sinh thái opensource đã hội tụ mạnh quanh **Whisper-stack** (faster-whisper / whisper.cpp / WhisperX, đều license MIT/BSD), trong khi NVIDIA NeMo (Canary/Parakeet) nổi lên như đối thủ vượt Whisper gốc về độ chính xác tiếng Pháp. Yếu tố quyết định chất lượng **không phải công cụ mà là lựa chọn model**: Whisper gốc small (~15–23% WER) không dùng được cho tiếng Pháp, nhưng fine-tune chuyên tiếng Pháp `bofenghuang/whisper-large-v3-french` đạt **~4.8% WER (FLEURS) / ~4.0% (MLS)** — đủ tốt để làm phụ đề thật với một vòng người review.

Bài toán thực sự không nằm ở khâu nhận dạng giọng nói (đã giải khá tốt) mà ở **ba điểm chốt**: (1) độ chính xác **timestamp** để phụ đề khớp hình — giải bằng forced-alignment của WhisperX; (2) khâu **dịch FR→VI** vốn là cặp low-resource, chất lượng dao động, bắt buộc có người/QE thẩm định; (3) **rủi ro pháp lý** — hai cạm bẫy thương mại là model dịch Meta (NLLB/SeamlessM4T, license CC-BY-NC cấm thương mại) và việc làm phụ đề cho video bên thứ ba không có bản quyền (tác phẩm phái sinh).

Xu hướng 2026+ là model đa phương thức một bước (audio → phụ đề đã dịch kèm timestamp, ví dụ Voxtral Transcribe 2) — đầy hứa hẹn nhưng độ chính xác timestamp tiếng Pháp **chưa được kiểm chứng độc lập**, nên pipeline cổ điển ASR→align→dịch vẫn là lựa chọn đáng tin cho tới khi có benchmark FR bên thứ ba.

**Key Findings:**

- **Model > công cụ:** chênh lệch WER tiếng Pháp giữa model gốc nhỏ và fine-tune large-v3 tiếng Pháp là **~3–5 lần**; đây là đòn bẩy chất lượng lớn nhất.
- **Timestamp là điểm yếu thật:** WhisperX (forced-align) cho timing tốt nhất, nhưng có lỗi đã biết với **chữ số** ("2014", "€13") — cần kiểm tra thủ công.
- **Audio `.avi` nhiễu** làm WER tăng **+10→+25%**; đa giọng +5→+10% → luôn cần vòng người review.
- **Pháp lý:** Meta NLLB/SeamlessM4T (CC-BY-NC) & `whisper-timestamped` (AGPL) là cạm bẫy thương mại/SaaS; xử lý local-only giảm mạnh rủi ro GDPR.
- **Lock-in thấp:** cùng trọng số large-v3 dùng lại qua mọi runtime; `.srt/.vtt` chuẩn phổ quát → giữ engine thay thế được sau interface `.srt` ổn định.

**Strategic Recommendations (Top 5):**

1. **Triển khai PA A** (WhisperX + fine-tune tiếng Pháp + llm-subtrans + Qwen2.5 Apache-2.0) làm pipeline mặc định.
2. **Benchmark trên dữ liệu thật của bạn** (~5–10 video `.avi`) trước khi scale — đo WER thủ công, kiểm timing chữ số.
3. **Thử nhánh dịch FR→EN→VI vs FR→VI trực tiếp**, chọn nhánh cho tiếng Việt tốt hơn.
4. **Bắt buộc vòng người review** trong quy trình — không giao đầu ra AI thô.
5. **Tránh model Meta CC-BY-NC & video không có bản quyền**; gắn nhãn "Phụ đề do AI tạo / dịch máy".

## Table of Contents

1. Research Overview & Domain Research Scope Confirmation _(đầu tài liệu)_
2. Industry Analysis — Bối cảnh công nghệ & benchmark WER tiếng Pháp
3. Competitive Landscape — So sánh chi tiết công cụ cho use case `.avi` batch
4. Regulatory Requirements — License, GDPR, EU AI Act, bản quyền
5. Technical Trends and Innovation — Xu hướng 2025–2026
6. Recommendations — PA A / PA B + lộ trình + giảm thiểu rủi ro
7. Research Synthesis _(mục này)_ — Executive Summary, bảng quyết định, next steps
8. Phụ lục — Bảng WER tổng hợp & nguồn chính

## Cross-Domain Synthesis — Kết nối liên ngành

- **Độ chính xác ↔ phần cứng:** WER tốt nhất tiếng Pháp (~4–5%) đòi model large-v3/Canary → cần GPU; CPU-only chỉ thực tế với model nhỏ hơn (WER cao hơn) hoặc chấp nhận chậm. _Mâu thuẫn cốt lõi của mục tiêu "local + chất lượng cao": cần GPU hoặc chấp nhận thời gian xử lý dài._
- **Độ chính xác ↔ pháp lý:** model dịch chất lượng cao FR↔đa ngữ (Meta SeamlessM4T/NLLB) lại vướng CC-BY-NC → buộc chọn LLM mở Apache-2.0 (Qwen2.5) cho luồng thương mại, đánh đổi chút chất lượng FR→VI lấy an toàn license.
- **Timestamp ↔ xu hướng:** model end-to-end mới (Voxtral) hấp dẫn nhưng chưa kiểm chứng timestamp FR → giữ kiến trúc tách lớp (ASR → align → dịch) để phòng hộ.
- **Batch ↔ lock-in:** thiết kế quanh interface `.srt` ổn định cho phép tráo engine (Whisper ↔ Canary) khi benchmark thực tế chỉ ra lựa chọn tốt hơn, không phải làm lại pipeline.

## Bảng quyết định chọn stack theo kịch bản

| Kịch bản phần cứng | Engine ASR khuyến nghị | Model | Dịch FR→VI/EN | Ghi chú |
|---|---|---|---|---|
| **CPU-only (không GPU)** | whisper.cpp _hoặc_ faster-whisper int8 | large-v3 (chậm) hoặc medium (nhanh hơn, WER cao hơn) | LLM local nhỏ (Qwen2.5-7B) hoặc API | Chấp nhận ~2.5–3h xử lý / 1h audio với large; ưu tiên batch qua đêm |
| **GPU ~8GB** | **WhisperX** (faster-whisper backend) | **bofenghuang/whisper-large-v3-french** (fp16) | llm-subtrans + Qwen2.5 Apache-2.0 | **PA A — khuyến nghị cho hầu hết trường hợp** |
| **GPU ≥16GB** | **NVIDIA Canary-1B-v2** | Canary-1B-v2 (WER FR ~4.86%) | llm-subtrans + LLM lớn hơn | PA B — WER tiếng Pháp tốt nhất; ghi công CC-BY-4.0 |
| **Batch rất lớn (100+ video)** | **NVIDIA Parakeet-TDT-0.6B-v3** | Parakeet-v3 (throughput cao nhất) | dịch theo lô qua vLLM | PA B — tối ưu tốc độ; chi phí "thoát" NeMo cao |

## Implementation Considerations — Lộ trình & next steps cho Rom

**Ngắn hạn (làm ngay — POC):**
1. Cài FFmpeg + faster-whisper + WhisperX; tải `bofenghuang/whisper-large-v3-french`.
2. Trích audio: `for f in *.avi; do ffmpeg -i "$f" -vn -ac 1 -ar 16000 -c:a pcm_s16le "${f%.avi}.wav"; done`
3. Chạy WhisperX trên 5–10 file thật → xuất `.srt` → **đo WER thủ công** trên vài đoạn, kiểm timing số/chữ số.
4. Dựng khâu dịch bằng llm-subtrans + Qwen2.5 (size Apache-2.0), so FR→VI trực tiếp vs FR→EN→VI.

**Trung hạn (scale + chất lượng):**
5. Thêm pass QE + chuẩn hóa tốc độ đọc/độ dài dòng tiếng Việt; chuẩn hóa quy trình người review.
6. Script batch resumable (đánh dấu file đã xong); song song hóa khâu FFmpeg (CPU) tách khỏi ASR (GPU).

**Theo dõi:**
7. Đánh giá lại Voxtral Transcribe 2 / Canary-Qwen khi có benchmark **timestamp tiếng Pháp** độc lập — có thể rút gọn pipeline.

## Research Methodology and Source Verification

**Phương pháp:** Nghiên cứu thực hiện qua 5 hướng web research song song (subagent), mỗi nhận định gắn nguồn URL; ưu tiên nguồn gốc (repo chính thức GitHub, model card Hugging Face, paper arXiv, leaderboard Open ASR, văn bản license gốc, trang chính thức GDPR/EU AI Act). Đa nguồn cho claim quan trọng; gắn cờ độ tin cậy.

**Độ tin cậy:**
- _Đã benchmark (tin cậy cao):_ bảng WER tiếng Pháp theo model size; Open ASR Leaderboard; tốc độ faster-whisper/CTranslate2; license (đọc trực tiếp văn bản gốc).
- _Ý kiến thực hành / định hướng (tin cậy trung bình):_ xếp hạng "tốt nhất cho phụ đề"; verdict tool dịch; WER large-v3-turbo tiếng Pháp.
- _Nhà cung cấp tự công bố / chưa kiểm chứng (tin cậy thấp):_ "Parakeet nhanh 10×"; timestamp FR của Voxtral Transcribe 2; tác động int8 lên WER tiếng Pháp; chất lượng FR→VI trực tiếp của model mở.

**Giới hạn:** Chưa có nguồn nào benchmark **tất cả engine trên độ chính xác timestamp phụ đề tiếng Pháp cụ thể** — đây là khoảng trống cần Rom tự benchmark trên dữ liệu thật. FR→VI là cặp low-resource ít được đo lường công khai. Phần pháp lý là tham khảo, **không phải tư vấn pháp lý** — cần luật sư xác nhận trước khi triển khai thương mại.

## Phụ lục — Bảng WER tiếng Pháp tổng hợp (tham chiếu nhanh)

| Model | Common Voice FR | MLS FR | FLEURS FR | Ghi chú |
|---|---|---|---|---|
| Whisper small (gốc) | 22.7 | 16.2 | 15.0 | Không dùng được cho phụ đề |
| Whisper medium (gốc) | 16.0 | 8.9 | 8.7 | Tạm, cần dọn nhiều |
| Whisper large-v2 (gốc) | 13.9 | 7.3 | 8.3 | — |
| Whisper large-v3 (gốc) | — | — | **6.59** | Tốt |
| large-v3-turbo (gốc) | — | — | ~7.7 | Tin cậy trung bình (1 benchmark) |
| **bofenghuang/whisper-medium-french** | 8.7 | 4.4 | 5.9 | Fine-tune FR |
| **bofenghuang/whisper-large-v3-french** | **7.28** | **3.98** | **4.84** | _Chất lượng cao nhất họ Whisper_ |
| NVIDIA Canary-1B-v2 | — | — | **4.86** | Vượt Whisper large-v3 gốc |
| NVIDIA Parakeet-TDT-0.6B-v3 | — | — | 5.38 | Throughput cao nhất |

**Nguồn chính:** Open ASR Leaderboard (arxiv 2510.06961v3) · bofenghuang model cards (HF) · openai/whisper · SYSTRAN/faster-whisper · m-bain/whisperX · ggerganov/whisper.cpp · NVIDIA NeMo (arxiv 2509.14128) · machinewrapped/llm-subtrans · Creative Commons CC-BY-NC 4.0 legal code · artificialintelligenceact.eu (Art. 50) · US Copyright Office AI Part 2 · 1qubit/Modal/Northflank benchmarks. _(URL đầy đủ trích dẫn trong từng mục tương ứng phía trên.)_

---

## Research Conclusion

**Summary of Key Findings:** Tạo phụ đề tiếng Pháp tự động chất lượng cao chạy local là khả thi và miễn phí với Whisper-stack + fine-tune tiếng Pháp; chất lượng do **lựa chọn model** quyết định (large-v3 fine-tune FR ~4.8% WER). Điểm khó thật là timestamp, dịch FR→VI low-resource, và rủi ro license/bản quyền.

**Strategic Impact:** Rom có thể dựng pipeline batch hoàn toàn opensource, an toàn thương mại (MIT/BSD/Apache), chạy offline (giảm rủi ro GDPR), với điều kiện giữ vòng người review và tránh hai cạm bẫy pháp lý đã nêu.

**Next Steps:** Bắt đầu với POC PA A trên dữ liệu `.avi` thật, đo WER + timing thực tế, rồi quyết định scale (giữ Whisper) hay chuyển NeMo (nếu cần WER FR tối đa / batch lớn).

---

**Research Completion Date:** 2026-05-19
**Source Verification:** Mọi nhận định được trích dẫn nguồn
**Confidence Level:** Cao — dựa trên nhiều nguồn độc lập có thẩm quyền (đã gắn cờ điểm tin cậy thấp)

_Tài liệu này là tham chiếu domain cho việc xây dựng pipeline phụ đề tiếng Pháp opensource + LLM; phần pháp lý không thay thế tư vấn luật sư._
