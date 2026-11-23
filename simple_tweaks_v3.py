import tkinter as tk
from tkinter import ttk, messagebox
import subprocess, json, platform, os, threading, datetime

APP_NAME = 'CART3R.JAILBREAK'
BG = '#0b1110'; PANEL = '#121c19'; PANEL2 = '#17231f'; GREEN = '#56e39a'; TEXT = '#edf5f0'; MUTED = '#91a69a'; RED = '#ff7777'

PS = 'powershell.exe'

def ps(command, timeout=20):
    if platform.system() != 'Windows':
        return False, 'Cette action nécessite Windows.'
    try:
        p = subprocess.run([PS, '-NoProfile', '-ExecutionPolicy', 'Bypass', '-Command', command], capture_output=True, text=True, timeout=timeout)
        return p.returncode == 0, (p.stdout or p.stderr).strip()
    except Exception as e:
        return False, str(e)

def is_admin():
    if platform.system() != 'Windows': return False
    ok, out = ps('[Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()').__class__ == tuple, ''
    try:
        p = subprocess.run([PS, '-NoProfile', '-Command', '[Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent() | ForEach-Object { $_.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator) }'], capture_output=True, text=True, timeout=5)
        return p.stdout.strip().lower() == 'true'
    except: return False

class App(tk.Tk):
    def __init__(self):
        super().__init__(); self.title(APP_NAME + ' — V3'); self.geometry('1180x760'); self.minsize(980,650); self.configure(bg=BG)
        self.admin = is_admin(); self.active = 'Dashboard'; self._style(); self._layout(); self.show_page('Dashboard')
    def _style(self):
        s=ttk.Style(self); s.theme_use('clam'); s.configure('Treeview', background=PANEL, foreground=TEXT, fieldbackground=PANEL, rowheight=28, borderwidth=0); s.configure('Treeview.Heading', background=PANEL2, foreground=GREEN, relief='flat')
    def _layout(self):
        top=tk.Frame(self,bg=BG); top.pack(fill='x',padx=24,pady=(18,10))
        tk.Label(top,text='ST',font=('Segoe UI',22,'bold'),fg=GREEN,bg=BG).pack(side='left')
        tk.Label(top,text='  CART3R.JAILBREAK',font=('Segoe UI',16,'bold'),fg=TEXT,bg=BG).pack(side='left')
        tk.Label(top,text='V3  •  PERFORMANCE CONTROL CENTER',font=('Segoe UI',9,'bold'),fg=MUTED,bg=BG).pack(side='left',padx=16,pady=8)
        self.admin_lbl=tk.Label(top,text=('ADMINISTRATEUR' if self.admin else 'MODE UTILISATEUR'),font=('Segoe UI',9,'bold'),fg=GREEN if self.admin else '#e6c36a',bg=PANEL,padx=12,pady=7); self.admin_lbl.pack(side='right')
        body=tk.Frame(self,bg=BG); body.pack(fill='both',expand=True,padx=20,pady=10)
        self.sidebar=tk.Frame(body,bg=PANEL,width=205); self.sidebar.pack(side='left',fill='y'); self.sidebar.pack_propagate(False)
        tk.Label(self.sidebar,text='ESPACE DE TRAVAIL',bg=PANEL,fg=MUTED,font=('Segoe UI',8,'bold')).pack(anchor='w',padx=17,pady=(20,10))
        self.nav={}
        for name,ico in [('Dashboard','▦'),('Simple Tweaks','◈'),('Windows OS','⚙'),('Gaming Profiles','▣'),('Network','⌁'),('FPS Test','◷'),('Restore Center','↶')]:
            b=tk.Button(self.sidebar,text=f'  {ico}   {name}',anchor='w',command=lambda n=name:self.show_page(n),bg=PANEL,fg=TEXT,activebackground=PANEL2,activeforeground=GREEN,relief='flat',bd=0,font=('Segoe UI',10),padx=10,pady=12,cursor='hand2'); b.pack(fill='x',padx=7,pady=2); self.nav[name]=b
        tk.Label(self.sidebar,text='SAFE BY DESIGN\nActions réversibles quand possible',bg=PANEL,fg=MUTED,font=('Segoe UI',8),justify='left').pack(side='bottom',anchor='w',padx=17,pady=18)
        self.content=tk.Frame(body,bg=BG); self.content.pack(side='left',fill='both',expand=True,padx=(18,0))
        self.status=tk.Label(self,text='Prêt • Les modifications système nécessitent parfois les droits administrateur.',bg=BG,fg=MUTED,anchor='w',font=('Segoe UI',8)); self.status.pack(fill='x',padx=25,pady=(0,12))
    def clear(self):
        for w in self.content.winfo_children(): w.destroy()
    def header(self,title,sub):
        tk.Label(self.content,text=title,bg=BG,fg=TEXT,font=('Segoe UI',23,'bold')).pack(anchor='w',pady=(8,2))
        tk.Label(self.content,text=sub,bg=BG,fg=MUTED,font=('Segoe UI',10)).pack(anchor='w',pady=(0,18))
    def card(self,parent,title,desc=None):
        f=tk.Frame(parent,bg=PANEL,padx=17,pady=14); f.pack(fill='x',pady=6)
        tk.Label(f,text=title,bg=PANEL,fg=TEXT,font=('Segoe UI',11,'bold')).pack(anchor='w')
        if desc: tk.Label(f,text=desc,bg=PANEL,fg=MUTED,font=('Segoe UI',9),wraplength=780,justify='left').pack(anchor='w',pady=(5,0))
        return f
    def button(self,parent,label,fn,primary=False):
        return tk.Button(parent,text=label,command=fn,bg=GREEN if primary else PANEL2,fg='#07110c' if primary else TEXT,activebackground='#8bf0b8',activeforeground='#07110c',relief='flat',bd=0,font=('Segoe UI',9,'bold'),padx=14,pady=9,cursor='hand2')
    def show_page(self,name):
        self.active=name; self.clear()
        for n,b in self.nav.items(): b.configure(bg=PANEL2 if n==name else PANEL,fg=GREEN if n==name else TEXT)
        getattr(self,'page_'+name.lower().replace(' ','_'))()
    def page_dashboard(self):
        self.header('Dashboard','Vue d’ensemble de ton PC et accès rapide aux outils.')
        grid=tk.Frame(self.content,bg=BG); grid.pack(fill='x')
        for title,val in [('CPU','Ryzen 5 5600'),('GPU','Radeon RX 6600 XT'),('OS',platform.platform().split('-')[0] if platform.system()=='Windows' else platform.system()),('Droits','Admin' if self.admin else 'Standard')]:
            c=tk.Frame(grid,bg=PANEL,padx=15,pady=15); c.pack(side='left',fill='x',expand=True,padx=(0,8)); tk.Label(c,text=title,bg=PANEL,fg=MUTED,font=('Segoe UI',9,'bold')).pack(anchor='w'); tk.Label(c,text=val,bg=PANEL,fg=GREEN if title!='Droits' or self.admin else '#e6c36a',font=('Segoe UI',12,'bold')).pack(anchor='w',pady=(7,0))
        c=self.card(self.content,'Analyse matérielle','Lecture des composants, mémoire, carte mère, BIOS, stockage, pilotes et version de Windows. Les températures et fréquences dépendent des capteurs accessibles.')
        self.button(c,'LANCER LE SCAN',self.scan_hardware,True).pack(anchor='e',pady=(10,0))
        c=self.card(self.content,'Configuration de référence','Profil initial préconfiguré pour Ryzen 5 5600 + RX 6600 XT. Le scan réel remplacera les informations estimées.')
        self.button(c,'Ouvrir Simple Tweaks',lambda:self.show_page('Simple Tweaks')).pack(side='left',pady=(10,0)); self.button(c,'Ouvrir Windows OS',lambda:self.show_page('Windows OS')).pack(side='left',padx=8,pady=(10,0))
        self.results=tk.Text(self.content,height=11,bg=PANEL,fg=TEXT,insertbackground=TEXT,relief='flat',font=('Consolas',9),padx=12,pady=10); self.results.pack(fill='both',expand=True,pady=(10,0)); self.results.insert('end','Aucun scan lancé.\n')
    def scan_hardware(self):
        self.results.delete('1.0','end'); self.results.insert('end','Analyse en cours…\n'); self.update_idletasks()
        if platform.system()!='Windows': self.results.insert('end','Le scan matériel complet est disponible sous Windows.'); return
        cmd="""$cpu=Get-CimInstance Win32_Processor | Select-Object -First 1 Name,NumberOfCores,NumberOfLogicalProcessors,MaxClockSpeed; $gpu=Get-CimInstance Win32_VideoController | Select-Object Name,DriverVersion; $ram=[math]::Round((Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory/1GB,1); $board=Get-CimInstance Win32_BaseBoard | Select-Object Manufacturer,Product; $bios=Get-CimInstance Win32_BIOS | Select-Object SMBIOSBIOSVersion; $os=Get-CimInstance Win32_OperatingSystem | Select-Object Caption,Version,BuildNumber; $disk=Get-CimInstance Win32_DiskDrive | Select-Object Model,@{N='SizeGB';E={[math]::Round($_.Size/1GB,0)}}; [pscustomobject]@{CPU=$cpu;GPU=$gpu;RAM_GB=$ram;Motherboard=$board;BIOS=$bios;Windows=$os;Disks=$disk} | ConvertTo-Json -Depth 5"""
        def work():
            ok,out=ps(cmd,35); self.after(0,lambda:self._scan_done(ok,out))
        threading.Thread(target=work,daemon=True).start()
    def _scan_done(self,ok,out):
        self.results.delete('1.0','end'); self.results.insert('end',out if ok else 'Échec du scan : '+out)
    def page_simple_tweaks(self):
        self.header('Simple Tweaks','Réglages gaming séparés des optimisations profondes de Windows.')
        items=[('Désactiver les captures en arrière-plan','Réduit les captures Xbox/Game DVR en arrière-plan.',"New-Item -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR' -Force | Out-Null; Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR' -Name AppCaptureEnabled -Type DWord -Value 0; New-Item -Path 'HKCU:\\System\\GameConfigStore' -Force | Out-Null; Set-ItemProperty -Path 'HKCU:\\System\\GameConfigStore' -Name GameDVR_Enabled -Type DWord -Value 0"),('Activer le mode Jeu Windows','Active le réglage Game Mode de Windows.',"New-Item -Path 'HKCU:\\Software\\Microsoft\\GameBar' -Force | Out-Null; Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\GameBar' -Name AutoGameModeEnabled -Type DWord -Value 1; Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\GameBar' -Name AllowAutoGameMode -Type DWord -Value 1")]
        for title,desc,cmd in items:
            c=self.card(self.content,title,desc); self.button(c,'APPLIQUER',lambda x=cmd,t=title:self.run_action(t,x),True).pack(anchor='e',pady=(10,0))
        c=self.card(self.content,'Important','Chaque réglage est indépendant. Les changements de registre sont limités au profil utilisateur. Un redémarrage ou une déconnexion peut être nécessaire.')
    def page_windows_os(self):
        self.header('Windows OS','Optimisations système distinctes des Simple Tweaks. Priorité à la stabilité, à la latence et aux performances soutenues.')
        items=[('Créer un point de restauration','À faire avant toute modification système.',"Checkpoint-Computer -Description 'CART3R_JAILBREAK_V3' -RestorePointType 'MODIFY_SETTINGS'"),('Activer le profil Haute performance','Sélectionne le plan Haute performance si disponible.',"powercfg /setactive SCHEME_MIN"),('Désactiver les effets de transparence','Réduit quelques effets visuels de l’interface.',"New-Item -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize' -Force | Out-Null; Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize' -Name EnableTransparency -Type DWord -Value 0"),('Optimiser les effets visuels','Privilégie les performances visuelles Windows.',"Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects' -Name VisualFXSetting -Type DWord -Value 2")]
        for title,desc,cmd in items:
            c=self.card(self.content,title,desc); self.button(c,'EXÉCUTER',lambda x=cmd,t=title:self.run_action(t,x,True),True).pack(anchor='e',pady=(10,0))
        c=self.card(self.content,'Microsoft Defender — protection','Defender reste activé par défaut. Le désactiver durablement réduit fortement la sécurité et peut être bloqué par la protection contre les falsifications. V3 ne le coupe pas automatiquement pour gagner quelques FPS.')
        tk.Label(c,text='ÉTAT : protection conservée',bg=PANEL,fg=GREEN,font=('Segoe UI',9,'bold')).pack(anchor='w',pady=(8,0))
        c=self.card(self.content,'À propos des optimisations','Aucun service Windows essentiel, Windows Update, pare-feu ou mécanisme de sécurité ne sera supprimé. Les gains dépendent de la configuration et certaines options peuvent ne rien changer aux FPS.')
    def page_gaming_profiles(self):
        self.header('Gaming Profiles','Réglages de préparation pour tes jeux. Aucun paramètre graphique du jeu n’est modifié automatiquement.')
        for game,desc in [('Fortnite','Profil compétitif : captures en arrière-plan désactivées, mode Jeu activé.'),('Warzone','Profil compétitif : mêmes réglages Windows de base, priorité à la stabilité.')]:
            c=self.card(self.content,game,desc); self.button(c,'APPLIQUER LE PROFIL',lambda g=game:self.apply_profile(g),True).pack(anchor='e',pady=(10,0))
    def page_network(self):
        self.header('Network','Diagnostic réseau et informations de base. Aucun DNS ou réglage TCP n’est forcé.')
        c=self.card(self.content,'Diagnostic réseau','Affiche les interfaces, adresses IP locales et état de la passerelle.'); self.button(c,'LANCER LE DIAGNOSTIC',self.network_scan,True).pack(anchor='e',pady=(10,0))
        self.netout=tk.Text(self.content,height=17,bg=PANEL,fg=TEXT,relief='flat',font=('Consolas',9),padx=12,pady=10); self.netout.pack(fill='both',expand=True,pady=8)
    def network_scan(self):
        if platform.system()!='Windows': out='Diagnostic disponible sous Windows.'
        else: _,out=ps('Get-NetIPConfiguration | Format-List InterfaceAlias,IPv4Address,IPv4DefaultGateway,DNSServer; ipconfig /all',20)
        self.netout.delete('1.0','end'); self.netout.insert('end',out)
    def page_fps_test(self):
        self.header('FPS Test','Journal de comparaison avant/après optimisation. Les FPS doivent être mesurés dans le même jeu, la même scène et les mêmes réglages.')
        c=self.card(self.content,'Mesure manuelle','Saisis les FPS moyens observés pendant un test identique.'); row=tk.Frame(c,bg=PANEL); row.pack(fill='x',pady=10)
        tk.Label(row,text='AVANT',bg=PANEL,fg=MUTED).pack(side='left'); self.before=tk.Entry(row,width=12,bg=PANEL2,fg=TEXT,insertbackground=TEXT,relief='flat'); self.before.pack(side='left',padx=8,ipady=7)
        tk.Label(row,text='APRÈS',bg=PANEL,fg=MUTED).pack(side='left',padx=(20,0)); self.afterv=tk.Entry(row,width=12,bg=PANEL2,fg=TEXT,insertbackground=TEXT,relief='flat'); self.afterv.pack(side='left',padx=8,ipady=7)
        self.fpsresult=tk.Label(c,text='Résultat : —',bg=PANEL,fg=GREEN,font=('Segoe UI',12,'bold')); self.fpsresult.pack(anchor='w',pady=8)
        self.button(c,'CALCULER LA DIFFÉRENCE',self.calc_fps,True).pack(anchor='e')
    def calc_fps(self):
        try:
            a=float(self.before.get()); b=float(self.afterv.get()); d=b-a; pct=(d/a*100) if a else 0
            self.fpsresult.config(text=f'Résultat : {d:+.1f} FPS  ({pct:+.1f} %)')
        except: messagebox.showerror('Valeurs invalides','Entre deux nombres valides.')
    def page_restore_center(self):
        self.header('Restore Center','Prépare un point de restauration avant les optimisations Windows.')
        c=self.card(self.content,'Créer un point de restauration','Windows peut désactiver la protection système ou refuser la création si elle n’est pas configurée.'); self.button(c,'CRÉER UN POINT',lambda:self.run_action('Point de restauration',"Checkpoint-Computer -Description 'CART3R_JAILBREAK_V3' -RestorePointType 'MODIFY_SETTINGS'",True),True).pack(anchor='e',pady=(10,0))
        c=self.card(self.content,'Annuler une modification','Utilise la restauration du système Windows pour revenir à un point antérieur. La V3 ne supprime pas automatiquement les points de restauration.')
        self.button(c,'OUVRIR LA RESTAURATION WINDOWS',lambda:ps('Start-Process rstrui.exe')).pack(anchor='e',pady=(10,0))
    def run_action(self,title,cmd,admin=False):
        if admin and not self.admin:
            messagebox.showwarning('Droits administrateur','Relance CART3R.JAILBREAK en tant qu’administrateur pour cette action.'); return
        if not messagebox.askyesno('Confirmer',f'Exécuter : {title} ?\n\nVérifie que tu souhaites appliquer ce changement.'): return
        ok,out=ps(cmd,35); self.status.config(text=(('Succès' if ok else 'Échec')+' • '+title+' • '+(out[:180] if out else 'Commande exécutée.')))
        messagebox.showinfo('Résultat',('Opération terminée.' if ok else 'La commande a échoué.')+'\n'+(out[:1000] if out else ''))
    def apply_profile(self,game):
        if not messagebox.askyesno('Appliquer le profil',f'Appliquer les réglages Windows de base pour {game} ?'): return
        commands=["New-Item -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR' -Force | Out-Null; Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR' -Name AppCaptureEnabled -Type DWord -Value 0", "New-Item -Path 'HKCU:\\Software\\Microsoft\\GameBar' -Force | Out-Null; Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\GameBar' -Name AutoGameModeEnabled -Type DWord -Value 1"]
        for cmd in commands: ps(cmd)
        messagebox.showinfo('Profil appliqué',f'Réglages Windows de base appliqués pour {game}. Redémarre le jeu si nécessaire.')

if __name__=='__main__':
    App().mainloop()
