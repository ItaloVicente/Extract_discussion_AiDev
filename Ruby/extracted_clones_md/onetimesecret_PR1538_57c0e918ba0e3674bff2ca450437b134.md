# 🔍 Clone Analysis | Project: onetimesecret | PR: #1538

- **Commit SHA:** `19ffca835c98e547ce45d4b330c82de824985111`
- **Clone Fingerprint:** `57c0e918ba0e3674bff2ca450437b134`
- **Categoria:** `mei`

---

## 🧑‍💻 Clone Par 1
**File:** `apps/api/v1/utils.rb`
**Lines:** 150 to 180

```text
def natural_time(time_in_s)
        return if time_in_s.nil?

        val = Time.now.utc.to_i - time_in_s.to_i
        # puts val
        if val < 10
          result = 'a moment ago'
        elsif val < 40
          result = "about #{(val * 1.5).to_i.to_s.slice(0, 1)}0 seconds ago"
        elsif val < 60
          result = 'about a minute ago'
        elsif val < 60 * 1.3
          result = '1 minute ago'
        elsif val < 60 * 2
          result = '2 minutes ago'
        elsif val < 60 * 50
          result = "#{(val / 60).to_i} minutes ago"
        elsif val < 3600 * 1.4
          result = 'about 1 hour ago'
        elsif val < 3600 * (24 / 1.02)
          result = "about #{(val / 60 / 60 * 1.02).to_i} hours ago"
        elsif val < 3600 * 24 * 1.6
          result = Time.at(time_in_s.to_i).strftime('yesterday').downcase
        elsif val < 3600 * 24 * 7
          result = Time.at(time_in_s.to_i).strftime('on %A').downcase
        else
          weeks = (val / 3600.0 / 24.0 / 7).to_i
          result = Time.at(time_in_s.to_i).strftime("#{weeks} #{'week'.plural(weeks)} ago").downcase
        end
        result
      end
```

---

## 🧑‍💻 Clone Par 2
**File:** `lib/onetime/utils.rb`
**Lines:** 392 to 424

```text
def natural_time(time_in_s)
      return if time_in_s.nil?

      val = Time.now.utc.to_i - time_in_s.to_i
      # puts val
      if val < 10
        result = 'a moment ago'
      elsif val < 40
        result = "about #{(val * 1.5).to_i.to_s.slice(0, 1)}0 seconds ago"
      elsif val < 60
        result = 'about a minute ago'
      elsif val < 60 * 1.3
        result = '1 minute ago'
      elsif val < 60 * 2
        result = '2 minutes ago'
      elsif val < 60 * 50
        result = "#{(val / 60).to_i} minutes ago"
      elsif val < 3600 * 1.4
        result = 'about 1 hour ago'
      elsif val < 3600 * (24 / 1.02)
        result = "about #{(val / 60 / 60 * 1.02).to_i} hours ago"
      elsif val < 3600 * 24 * 1.6
        result = Time.at(time_in_s.to_i).strftime('yesterday').downcase
      elsif val < 3600 * 24 * 7
        result = Time.at(time_in_s.to_i).strftime('on %A').downcase
      else
        weeks  = (val / 3600.0 / 24.0 / 7).to_i
        result = Time.at(time_in_s.to_i)
          .strftime("#{weeks} #{'week'.plural(weeks)} ago")
          .downcase
      end
      result
    end
```

