# 🔍 Clone Analysis | Project: java-util | PR: #184

- **Commit SHA:** `ac9f77046f28f7ff507ccc8406b0470e65dbb988`
- **Clone Fingerprint:** `df8ab4ba283ce08c2dd2a97c4f3789bf`
- **Categoria:** `unique_final`

---

## 🧑‍💻 Clone Par 1
**File:** `src/main/java/com/cedarsoftware/util/EncryptionUtilities.java`
**Lines:** 600 to 623

```text
public static String decrypt(String key, String hexStr) {
        if (key == null || hexStr == null) {
            throw new IllegalArgumentException("key and hexStr cannot be null");
        }
        byte[] data = ByteUtilities.decode(hexStr);
        if (data == null || data.length == 0) {
            throw new IllegalArgumentException("Invalid hexadecimal input");
        }
        try {
            if (data[0] == 1 && data.length > 29) {
                byte[] salt = Arrays.copyOfRange(data, 1, 17);
                byte[] iv = Arrays.copyOfRange(data, 17, 29);
                byte[] cipherText = Arrays.copyOfRange(data, 29, data.length);

                SecretKeySpec sKey = new SecretKeySpec(deriveKey(key, salt, 128), "AES");
                Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
                cipher.init(Cipher.DECRYPT_MODE, sKey, new GCMParameterSpec(128, iv));
                return new String(cipher.doFinal(cipherText), StandardCharsets.UTF_8);
            }
            return new String(createAesDecryptionCipher(key).doFinal(data), StandardCharsets.UTF_8);
        } catch (Exception e) {
            throw new IllegalStateException("Error occurred decrypting data", e);
        }
    }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/main/java/com/cedarsoftware/util/EncryptionUtilities.java`
**Lines:** 633 to 656

```text
public static byte[] decryptBytes(String key, String hexStr) {
        if (key == null || hexStr == null) {
            throw new IllegalArgumentException("key and hexStr cannot be null");
        }
        byte[] data = ByteUtilities.decode(hexStr);
        if (data == null || data.length == 0) {
            throw new IllegalArgumentException("Invalid hexadecimal input");
        }
        try {
            if (data[0] == 1 && data.length > 29) {
                byte[] salt = Arrays.copyOfRange(data, 1, 17);
                byte[] iv = Arrays.copyOfRange(data, 17, 29);
                byte[] cipherText = Arrays.copyOfRange(data, 29, data.length);

                SecretKeySpec sKey = new SecretKeySpec(deriveKey(key, salt, 128), "AES");
                Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
                cipher.init(Cipher.DECRYPT_MODE, sKey, new GCMParameterSpec(128, iv));
                return cipher.doFinal(cipherText);
            }
            return createAesDecryptionCipher(key).doFinal(data);
        } catch (Exception e) {
            throw new IllegalStateException("Error occurred decrypting data", e);
        }
    }
```

