import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { Presentation, PresentationFile } from "@oai/artifact-tool";

const workspaceDir = "/Users/Janice/Desktop/Git Hub workspace/personal-project";
const targetDir = path.join(workspaceDir, "school-notes/machine-learning-and-decisions");
const buildDir = path.join(workspaceDir, ".codex-ppt-build");
const skillDir = "/Users/Janice/.codex/plugins/cache/openai-primary-runtime/presentations/26.1112.11217/skills/presentations";
const pythonExecutable = "/Users/Janice/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3";
const { finalizePresentation } = await import(pathToFileURL(path.join(skillDir, "container_tools/artifact_tool_utils.mjs")).href);

const FONT = "PingFang TC";
const CODE = "Menlo";
const C = { navy: "#102A43", teal: "#0F766E", aqua: "#5EEAD4", ink: "#172B4D", gray: "#52616B", pale: "#F3F8FA", white: "#FFFFFF", line: "#C9D8DE", amber: "#D97706", red: "#B42318" };

const slides = [
  {n:1,t:"第五章 大語言模型",sub:"從 Llama 2 訓練到權重檔解析",cover:true,b:["《大語言模型開發》章節教學簡報","報告者：Janice"],notes:"本章的焦點是開源大語言模型的訓練、模型結構、權重檔與參數計算。來源：課本 p.124–125。"},
  {n:2,t:"本章的三個層次",b:["模型層：Llama 2 如何預訓練與對齊","結構層：解碼器層由哪些模組組成","檔案層：數十億參數如何儲存與載入"],flow:["模型","結構","檔案"],notes:"先建立章節地圖。解碼器層是 Llama 重複堆疊的主要運算單元，包含注意力機制與前饋網路。"},
  {n:3,t:"大語言模型的主要特徵",b:["使用大規模文字資料進行自監督預訓練","使用更深、更寬的轉換器網路架構","能生成連貫文字，而不只輸出分類標籤","能把預訓練知識運用到多種任務","沒有示範也能執行任務；提供少量示範後也能模仿"],notes:"轉換器網路英文為 Transformer，能讓模型比較句子中不同位置的資訊。沒有示範稱零樣本學習；提供少量示範稱少樣本學習。來源：課本 p.125，5.1。"},
  {n:4,t:"GPT、ChatGPT 與 Llama 的角色",cols:[{h:"GPT",x:"逐步預測下一個詞元的預訓練語言模型家族"},{h:"ChatGPT",x:"在 GPT 基礎上加入對話微調與人類偏好對齊"},{h:"Llama",x:"Meta 公開權重的大語言模型家族，適合研究與本地開發"}],notes:"詞元是模型實際讀取的文字單位，可能是一個字、詞的一部分或符號。課本對 GPT-3.5 的架構數字不一致，因此不作為計算依據。"},
  {n:5,t:"Llama 1 模型家族",table:[["模型版本","隱藏層維度","層數","訓練詞元數"],["6.7B","4096","32","1.0 兆"],["13.0B","5120","40","1.0 兆"],["32.5B","6656","60","1.4 兆"],["65.2B","8192","80","1.4 兆"]],notes:"B 代表十億個參數，不是檔案容量。隱藏層維度代表模型用多少個數字表示一個詞元。來源：課本 p.126，表 5-1。"},
  {n:6,t:"Llama 2 相較 Llama 1 的改變",table:[["項目","Llama 1","Llama 2"],["訓練資料量","1.4 兆詞元","2.0 兆詞元"],["上下文長度","2048","4096"],["最大模型版本","65B","70B"],["注意力機制","多頭注意力","70B 使用分組查詢注意力"]],notes:"上下文長度表示模型一次可以處理多少詞元。分組查詢注意力會讓多組查詢共用較少的鍵和值，降低推理成本。來源：課本 p.127、p.132。"},
  {n:7,t:"Llama 2 的訓練設定與文字切分",extra:true,b:["使用 AdamW 方法更新模型參數","前 2,000 步逐漸提高學習率，避免一開始更新過大","之後依餘弦曲線逐步降低學習率","文字切分器使用約 32,000 個詞元的詞彙表","遇到未知字元時退回到位元組層級處理"],notes:"文字切分器英文為 tokenizer，負責把文字切成模型能讀取的詞元編號。AdamW 是常用的參數更新方法。來源：課本 p.127。"},
  {n:8,t:"Llama 1 預訓練資料組成",bars:[["CommonCrawl",67],["C4",15],["GitHub",4.5],["Wikipedia",4.5],["Books",4.5],["arXiv",2.5],["Stack Exchange",2]],notes:"比例小不等於不重要。GitHub 與 arXiv 提供程式碼及數理文本。來源：課本 p.128，表 5-3。"},
  {n:9,t:"資料清洗決定模型吃進什麼",b:["CommonCrawl：去重、語言辨識、品質過濾","GitHub：授權篩選、品質規則、檔案去重","Books：移除高度重疊的書籍","arXiv：清理前置內容、註解與參考文獻","Stack Exchange：去除 HTML，依分數整理回答"],notes:"重複資料會降低有效多樣性，也可能增加記憶風險。來源：課本 p.128–129。"},
  {n:10,t:"Llama 2 訓練 loss 曲線",big:"2T token 後，四種模型的 training loss 仍持續下降",b:["x 軸：已處理的 token 數","y 軸：training loss","曲線未飽和不等於所有下游任務都等比例提升"],notes:"來源：課本 p.129，圖 5-1。"},
  {n:11,t:"Base model 到 Chat model",flow:["Llama 2 base","SFT","Reward model","RLHF","Llama 2-Chat"],notes:"預訓練先學語言與知識，對齊階段再學如何依指令回答。來源：課本 p.130–132。"},
  {n:12,t:"SFT 只對回答區域計算 loss",code:"prompt = [系統指令 + 使用者問題]   # mask\nanswer = [模型應學習的回答]         # calculate loss",b:["Meta 使用 27,540 筆高品質人工撰寫資料","序列長度為 4096","prompt token 不參與本章描述的 loss 計算"],notes:"來源：課本 p.130，5.5.1。"},
  {n:13,t:"人類偏好資料的收集方式",extra:true,cols:[{h:"回答 A",x:"針對同一 prompt 生成的候選答案"},{h:"回答 B",x:"另一個候選答案"}],b:["標註者選擇較佳回答","並標示偏好強度：顯著較好、較好、稍好或不確定"],notes:"完整版加講。偏好資料不是標準答案，而是兩個回答之間的比較。來源：課本 p.130–131。"},
  {n:14,t:"Helpfulness 與 Safety 分開建模",cols:[{h:"Helpfulness RM",x:"Meta Helpfulness : (Meta Safety + 開源) = 1 : 1"},{h:"Safety RM",x:"Meta Safety : (Meta Helpfulness + 開源) = 9 : 1"}],notes:"一個分數很難同時處理有用與安全的衝突，因此分開訓練。來源：課本 p.131。"},
  {n:15,t:"Rejection Sampling 與 PPO",extra:true,cols:[{h:"Rejection sampling",x:"同一 prompt 生成 K 個候選，挑 reward 較高者"},{h:"PPO",x:"依 reward 進行策略梯度更新"}],notes:"完整版加講。課本以寬度和深度解釋兩種更新方式。來源：課本 p.131–132。"},
  {n:16,t:"以程式讀入 Llama 2 結構",code:'from transformers import AutoModelForCausalLM\nimport torch\n\nmodel = AutoModelForCausalLM.from_pretrained(\n    "C:/llama2/llama-2-7b-hf",\n    torch_dtype=torch.float16,\n    device_map="cpu",\n)\nprint(model)',notes:"課本附碼：第5章 大语言模型.ipynb 第一個 code cell。目的在印出模型結構，不是生成文字。"},
  {n:17,t:"LlamaForCausalLM 的外層結構",tree:["LlamaForCausalLM","model: LlamaModel","layers: 32 × LlamaDecoderLayer","lm_head: 4096 → 32000"],notes:"AutoModel 只有 backbone；AutoModelForCausalLM 還包含把 hidden state 映射回 vocabulary logits 的 lm_head。來源：課本 p.132–133。"},
  {n:18,t:"一個 Decoder Layer 的模組",cols:[{h:"Self-Attention",x:"q_proj、k_proj、v_proj、o_proj 與 RoPE"},{h:"SwiGLU MLP",x:"gate_proj、up_proj、down_proj 與 SiLU"},{h:"RMSNorm",x:"input_layernorm 與 post_attention_layernorm"}],notes:"先辨認模組名稱，再進入參數計算。來源：課本 p.132–133。"},
  {n:19,t:"7B 與 70B 的 attention shape",extra:true,table:[["投影","7B","70B"],["q_proj","[4096,4096]","[8192,8192]"],["k_proj","[4096,4096]","[1024,8192]"],["v_proj","[4096,4096]","[1024,8192]"],["o_proj","[4096,4096]","[8192,8192]"]],notes:"完整版加講。70B 的 K/V 輸出縮到 1024，反映 GQA。來源：課本 p.138，表 5-6。"},
  {n:20,t:"原始 pth 與 Hugging Face 格式",cols:[{h:"原始 pth",x:"consolidated.00.pth\nparams.json\nchecklist.chk"},{h:"Hugging Face",x:"config.json\ntokenizer 檔\nindex JSON\n多個 .bin shard"}],notes:"模型至少包含架構設定、tokenizer、生成設定與權重。來源：課本 p.134–136。"},
  {n:21,t:"Sharded checkpoint 與 index JSON",code:'"model.layers.0.self_attn.q_proj.weight":\n  "pytorch_model-00001-of-00002.bin"\n\n"lm_head.weight":\n  "pytorch_model-00002-of-00002.bin"',b:["index JSON 記錄參數名稱與 shard 檔名","載入器依索引找到每個 tensor","10 GB 是舊範例的分片設定，不是永遠固定的規則"],notes:"來源：課本 p.134、p.140。"},
  {n:22,t:"參數量就是矩陣元素數",big:"Linear(4096, 11008, bias=False)",code:"4096 × 11008 = 45,088,768 parameters",b:["shape 相乘就是 weight 元素數","bias=False，因此不用再加 11,008 個 bias"],notes:"來源：課本 p.136–138。"},
  {n:23,t:"每層 Attention 與 MLP 的參數",cols:[{h:"MHA",x:"4d²\n來自 Q、K、V、O 四個矩陣"},{h:"SwiGLU MLP",x:"3d × d_ff\n來自 gate、up、down 三個矩陣"}],b:["每層還有兩個長度為 d 的 RMSNorm 向量"],notes:"代入 7B 維度，比較 attention 與 MLP 的參數量。來源：課本 p.138。"},
  {n:24,t:"Llama 2 7B 參數量的程式計算",code:"V = 32000\nd_model = 4096\nd_ff = 11008\nL = 32\n\nnparams = (V*d_model\n  + L*(4*d_model**2 + 3*d_ff*d_model + 2*d_model + 64)\n  + d_model + V*d_model)\nprint(nparams)  # 6,738,417,664",notes:"課本附碼：第5章 计算参数量.ipynb 第一個 code cell。+64 對應 inv_freq，但不同版本可能把它當 buffer。"},
  {n:25,t:"公式與 API 為何得到不同數字",code:'from transformers import AutoModel\n\nmodel = AutoModel.from_pretrained(\n    "c:/llama2/llama-2-7b-hf"\n)\ntotal_params = sum(p.numel() for p in model.parameters())',b:["AutoModel 沒有 lm_head","AutoModelForCausalLM 包含 lm_head","buffer 不一定出現在 model.parameters()","weight tying 也會影響統計口徑"],notes:"課本附碼：兩份第五章 Notebook 的參數統計 cell。"},
  {n:26,t:"參數、檔案大小與顯存",cols:[{h:"參數量",x:"模型中需要儲存的元素個數"},{h:"權重位元組",x:"元素數 × 每個元素的位元組數"},{h:"檔案大小",x:"權重 + 檔案容器 + 中繼資料"},{h:"執行顯存",x:"權重 + 中間運算結果 + 鍵值快取 + 框架配置"}],big:"6,738,417,664 個 16 位元浮點參數 ≈ 13.48 GB ≈ 12.55 GiB",notes:"模型檔案大小不能直接當作最低顯示記憶體需求。"},
  {n:27,t:"PyTorch .bin 的 ZIP 結構",extra:true,flow:[".bin / ZIP","data.pkl","data/0, data/1, …"],b:["data.pkl：Python 物件與 tensor metadata","data/*：大型 storage payload"],notes:"完整版加講。來源：課本 p.140，圖 5-4、5-5。"},
  {n:28,t:"pickle 反序列化的攔截點",extra:true,cols:[{h:"persistent_load(pid)",x:"遇到 storage reference 時改回傳 LazyStorage"},{h:"find_class(module, name)",x:"決定類別與 tensor 重建函式如何解析"}],b:["安全提醒：不要對不可信來源直接 pickle.load()"],notes:"完整版加講。來源：課本 p.140–142。"},
  {n:29,t:"LazyUnpickler 的核心程式",code:'def persistent_load(self, pid):\n    assert pid[0] == "storage"\n    data_type = pid[1].data_type\n    filename = self.data_base_path + "/" + pid[2]\n    return LazyStorage(pid[1], filename)\n\ndef lazy_rebuild_tensor_v2(storage, offset, size, stride,\n                           requires_grad, hooks, metadata=None):\n    return LazyTensor(list(size), storage.kind.data_type,\n                      f"offset={offset}")',notes:"課本附碼：第5章 大语言模型.ipynb 第二個 code cell。只建立 shape、dtype、offset 等 metadata。Notebook 中 @staticmethod 被註解，實際使用前應修正。"},
  {n:30,t:"只靠 metadata 計算參數與 bytes",code:'for name, tensor in state.items():\n    count = math.prod(tensor.shape)\n    n_params += count\n    n_bytes += count * (\n        4 if tensor.data_type == DT_F32 else 2\n    )',b:["不用讀入完整 tensor payload","math.prod(shape) 可處理任意維 tensor","這套方法只適用 pickle-based .bin，不直接適用 safetensors"],notes:"改寫自課本附贈 Notebook 的 nParams / nBytes 迴圈。來源：課本 p.143–144。"},
  {n:31,t:"第五章的完整鏈條",flow:["訓練資料","Llama 2 base","SFT / RLHF","模型模組","checkpoint","metadata / bytes"],b:["Chat model 在 base model 上再進行對齊","參數量可由 shape 推導，也能用 API 驗證","checkpoint 是結構化容器，不只是巨大檔案"],notes:"總結全章。延伸閱讀可研究 safetensors、量化、LoRA 與 RAG，但不屬於第五章主體。"},
];

function box(slide, left, top, width, height, fill="none", line="none", radius=false) {
  return slide.shapes.add({geometry: radius ? "roundRect" : "rect", position:{left,top,width,height}, fill, line:{style:"solid",fill:line,width:line==="none"?0:1}, borderRadius: radius?"rounded-xl":undefined});
}
function text(slide, value, p, size=26, color=C.ink, bold=false, family=FONT, align="left") {
  const s=slide.shapes.add({geometry:"textbox",position:p,fill:"none",line:{style:"solid",fill:"none",width:0}});
  s.text=value; s.text.style={fontSize:size,color,bold,typeface:family,alignment:align,verticalAlignment:"middle",autoFit:"shrinkText"}; return s;
}
function bullets(slide, items, p, size=25) {
  const value=items.map((x,i)=>`${i+1}. ${x}`).join("\n"); return text(slide,value,p,size,C.ink,false,FONT,"left");
}
function header(slide,d,index,total) {
  slide.background.fill=C.pale;
  box(slide,0,0,18,720,C.teal,"none");
  text(slide,d.t,{left:64,top:36,width:1080,height:58},34,C.navy,true);
  box(slide,64,104,150,4,C.aqua,"none");
  text(slide,`${String(index).padStart(2,"0")} / ${total}`,{left:1110,top:44,width:110,height:32},14,C.gray,false,FONT,"right");
}
function addFlow(slide,items,top=250) {
  const gap=16, left=70, totalW=1140, w=(totalW-gap*(items.length-1))/items.length;
  items.forEach((it,i)=>{box(slide,left+i*(w+gap),top,w,92,i===items.length-1?C.teal:C.white,C.line,true);text(slide,it,{left:left+i*(w+gap)+10,top:top+12,width:w-20,height:68},22,i===items.length-1?C.white:C.navy,true,FONT,"center"); if(i<items.length-1) text(slide,"→",{left:left+i*(w+gap)+w,top:top+23,width:gap,height:45},24,C.teal,true,FONT,"center");});
}
function addTable(slide,rows) {
  const top=150,left=80,width=1120,rowH=Math.min(72,450/rows.length),cols=rows[0].length,colW=width/cols;
  rows.forEach((r,ri)=>r.forEach((v,ci)=>{box(slide,left+ci*colW,top+ri*rowH,colW,rowH,ri===0?C.navy:(ri%2?C.white:"#EAF3F4"),C.line);text(slide,String(v),{left:left+ci*colW+8,top:top+ri*rowH+5,width:colW-16,height:rowH-10},ri===0?19:18,ri===0?C.white:C.ink,ri===0,FONT,"center");}));
}
function addCode(slide,code,top=150,height=420,left=72,width=1136) {
  box(slide,left,top,width,height,"#0B1F33","#24465F",true);
  text(slide,code,{left:left+28,top:top+20,width:width-56,height:height-40},20,"#DFF7F3",false,CODE,"left");
}
function addSlide(presentation,d,index,total) {
  const slide=presentation.slides.add();
  if(d.cover){slide.background.fill=`linear(135deg, ${C.navy} 0%, #163F59 60%, ${C.teal} 100%)`;text(slide,d.t,{left:86,top:160,width:950,height:92},54,C.white,true);text(slide,d.sub,{left:90,top:270,width:900,height:60},28,C.aqua,false);box(slide,90,360,150,5,C.aqua,"none");text(slide,d.b.join("\n"),{left:90,top:400,width:780,height:100},21,"#D7E6EB",false);text(slide,"05",{left:1000,top:480,width:180,height:120},86,"#5EEAD4",true,FONT,"center");}
  else {header(slide,d,index,total);
    if(d.big) text(slide,d.big,{left:80,top:126,width:1120,height:82},30,C.teal,true,FONT,"center");
    if(d.code && d.b) addCode(slide,d.code,d.big?235:145,d.big?365:420,72,690);
    else if(d.code) addCode(slide,d.code,d.big?230:140,460);
    else if(d.table) addTable(slide,d.table);
    else if(d.bars){const max=67;d.bars.forEach((r,i)=>{const y=142+i*68;text(slide,r[0],{left:80,top:y,width:200,height:34},20,C.ink,i<2);box(slide,295,y,Math.max(10,780*r[1]/max),34,i<2?C.teal:"#6EA8A4","none",true);text(slide,`${r[1]}%`,{left:1085,top:y,width:100,height:34},18,C.navy,true,FONT,"right");});}
    else if(d.table) addTable(slide,d.table);
    else if(d.cols){const count=d.cols.length,gap=24,left=76,w=(1128-gap*(count-1))/count,cardTop=d.big?240:160;d.cols.forEach((c,i)=>{const x=left+i*(w+gap);box(slide,x,cardTop,w,270,C.white,C.line,true);text(slide,c.h,{left:x+20,top:cardTop+25,width:w-40,height:55},24,C.teal,true,FONT,"center");box(slide,x+24,cardTop+92,w-48,3,C.aqua,"none");text(slide,c.x,{left:x+24,top:cardTop+118,width:w-48,height:125},20,C.ink,false,FONT,"center");});}
    else if(d.flow) addFlow(slide,d.flow,d.b?210:270);
    else if(d.tree){d.tree.forEach((v,i)=>{const x=120+i*70,y=145+i*105,w=1040-i*140;box(slide,x,y,w,68,i===0?C.navy:(i===d.tree.length-1?C.teal:C.white),C.line,true);text(slide,v,{left:x+20,top:y+8,width:w-40,height:52},22,i===0||i===d.tree.length-1?C.white:C.ink,true,FONT,"center");});}
    if(d.b && !d.code){const top=d.flow?360:(d.cols?470:(d.big?235:145));bullets(slide,d.b,{left:92,top,width:1090,height:540-top},d.b.length>4?22:24);}
    if(d.b && d.code){bullets(slide,d.b,{left:800,top:d.big?245:160,width:390,height:d.big?330:430},20);}
  }
  slide.speakerNotes.text=d.notes||"";
  return slide;
}

async function build(name,filter) {
  const selected=slides.filter(filter); const p=Presentation.create({slideSize:{width:1280,height:720}});
  selected.forEach((d,i)=>addSlide(p,d,i+1,selected.length));
  const previewDir=path.join(buildDir,`preview-${name}`);await fs.mkdir(previewDir,{recursive:true});
  for(let i=0;i<p.slides.items.length;i++){const blob=await p.export({slide:p.slides.items[i],format:"png",scale:1});await fs.writeFile(path.join(previewDir,`slide-${String(i+1).padStart(2,"0")}.png`),new Uint8Array(await blob.arrayBuffer()));}
  const montage=await p.export({format:"webp",montage:true});await fs.writeFile(path.join(buildDir,`${name}-montage.webp`),new Uint8Array(await montage.arrayBuffer()));
  const staging=path.join(buildDir,`staging-${name}`);await fs.mkdir(staging,{recursive:true});
  const candidate=path.join(staging,"candidate.pptx");await (await PresentationFile.exportPptx(p)).save(candidate);
  const finalPath=path.join(targetDir,`${name}.pptx`);
  const result=await finalizePresentation({workspaceDir,candidatePath:candidate,finalPath,pythonExecutable,integrityValidatorPath:path.join(skillDir,"container_tools/inspect_presentation_package_integrity.py"),layoutValidatorPath:path.join(skillDir,"container_tools/inspect_presentation_layout_geometry.py"),layoutArgs:["--expected-slide-size-emu","12192000,6858000","--validate-heading-fit"],explicitTotalSlideCount:selected.length,requiredNativeTableOwnerSlides:[],requiredNativeChartOwnerSlides:[],fontPolicy:{basis:"design",families:[FONT,CODE]},verifyArtifactToolImport:true,receiptPath:path.join(staging,"validation.json")});
  return {finalPath,slides:selected.length,result};
}

await fs.mkdir(buildDir,{recursive:true});await fs.mkdir(targetDir,{recursive:true});
const full=await build("第五章_完整版",()=>true);
const concise=await build("第五章_精簡版",d=>!d.extra);
console.log(JSON.stringify({full,concise},null,2));
