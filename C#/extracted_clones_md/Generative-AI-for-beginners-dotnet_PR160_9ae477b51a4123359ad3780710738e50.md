# 🔍 Clone Analysis | Project: Generative-AI-for-beginners-dotnet | PR: #160

- **Commit SHA:** `bf57ab373ed8b9852206fae95714c5b734d23eaf`
- **Clone Fingerprint:** `9ae477b51a4123359ad3780710738e50`
- **Categoria:** `mei_final`

---

## 🧑‍💻 Clone Par 1
**File:** `translations/de/03-CoreGenerativeAITechniques/src/VideosHelper.cs`
**Lines:** 72 to 92

```text
static string FindVideosFolder(string startDirectory)
    {
        var currentDirectory = startDirectory;

        while (true)
        {
            var potentialVideos = Path.Combine(currentDirectory, "videos");
            if (Directory.Exists(potentialVideos))
            {
                return potentialVideos;
            }

            var parentDirectory = Directory.GetParent(currentDirectory);
            if (parentDirectory == null)
            {
                throw new DirectoryNotFoundException("The 'videos' folder was not found in any parent directory.");
            }

            currentDirectory = parentDirectory.FullName;
        }
    }
```

---

## 🧑‍💻 Clone Par 2
**File:** `03-CoreGenerativeAITechniques/src/VideosHelper.cs`
**Lines:** 72 to 92

```text
static string FindVideosFolder(string startDirectory)
    {
        var currentDirectory = startDirectory;

        while (true)
        {
            var potentialVideos = Path.Combine(currentDirectory, "videos");
            if (Directory.Exists(potentialVideos))
            {
                return potentialVideos;
            }

            var parentDirectory = Directory.GetParent(currentDirectory);
            if (parentDirectory == null)
            {
                throw new DirectoryNotFoundException("The 'videos' folder was not found in any parent directory.");
            }

            currentDirectory = parentDirectory.FullName;
        }
    }
```

