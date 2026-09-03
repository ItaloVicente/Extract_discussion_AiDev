# 🔍 Clone Analysis | Project: OCTGN | PR: #2250

- **Commit SHA:** `ef43e3eabb8a8336546716e39241fc4843ff525a`
- **Clone Fingerprint:** `ccd56aa053c36ca3cc0b9a005bf8ff1a`
- **Categoria:** `unique_ini`

---

## 🧑‍💻 Clone Par 1
**File:** `octgnFX/Octgn.JodsEngine/Scripting/Versions/Script_3_1_0_2.cs`
**Lines:** 428 to 452

```text
private bool CanViewPileInScript(Pile pile)
        {
            // If the player owns the pile, they can always view it
            if (pile.Owner == Player.LocalPlayer)
                return true;
                
            switch (pile.ProtectionState)
            {
                case GroupProtectionState.False:
                    return true;
                    
                case GroupProtectionState.True:
                    Program.GameMess.Warning($"Cannot view {pile.FullName} - it is protected.");
                    return false;
                    
                case GroupProtectionState.Ask:
                    // Post a message asking for permission
                    Program.GameMess.PlayerEvent(Player.LocalPlayer, $"requests permission to view {pile.FullName}");
                    Program.GameMess.Warning($"Permission requested to view {pile.FullName}. Waiting for {pile.Owner.Name} to grant access.");
                    return false;
                    
                default:
                    return true;
            }
        }
```

---

## 🧑‍💻 Clone Par 2
**File:** `octgnFX/Octgn.JodsEngine/Play/Gui/PileBaseControl.cs`
**Lines:** 80 to 110

```text
private bool CanViewPile(Pile pile)
        {
            // If the player owns the pile, they can always view it
            if (pile.Owner == Player.LocalPlayer)
                return true;
                
            switch (pile.ProtectionState)
            {
                case GroupProtectionState.False:
                    return true;
                    
                case GroupProtectionState.True:
                    Program.GameMess.Warning($"Cannot view {pile.FullName} - it is protected.");
                    return false;
                    
                case GroupProtectionState.Ask:
                    // Check if we have temporary permission
                    if (pile.TemporaryViewPermissions.Contains(Player.LocalPlayer))
                    {
                        return true;
                    }
                    
                    // Send network request for permission
                    Program.Client.Rpc.RequestPileViewPermission(pile, Player.LocalPlayer);
                    Program.GameMess.Warning($"Permission requested to view {pile.FullName}. Waiting for {pile.Owner.Name} to grant access.");
                    return false;
                    
                default:
                    return true;
            }
        }
```

