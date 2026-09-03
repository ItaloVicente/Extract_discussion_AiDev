# 🔍 Clone Analysis | Project: middleman-syntax | PR: #92

- **Commit SHA:** `1beced2ba1a0cf3fc64aac421d79e627ce75ffa1`
- **Clone Fingerprint:** `c6120d307683ced006324c3a67c03c15`
- **Categoria:** `ini_mei`

---

## 🧑‍💻 Clone Par 1
**File:** `vendor/bundle/ruby/3.2.0/gems/yard-0.9.37/templates/guide/method/html/setup.rb`
**Lines:** 6 to 22

```text
def format_args(object)
  return if object.parameters.nil?
  params = object.parameters
  if object.has_tag?(:yield) || object.has_tag?(:yieldparam)
    params.reject! do |param|
      param[0].to_s[0, 1] == "&" &&
        !object.tags(:param).any? {|t| t.name == param[0][1..-1] }
    end
  end

  if params.empty?
    ""
  else
    args = params.map {|n, v| v ? "<em>#{h n}</em> = #{h v}" : "<em>" + n.to_s + "</em>" }.join(", ")
    args
  end
end
```

---

## 🧑‍💻 Clone Par 2
**File:** `vendor/bundle/ruby/3.2.0/gems/yard-0.9.37/lib/yard/templates/helpers/method_helper.rb`
**Lines:** 7 to 25

```text
def format_args(object)
        return if object.parameters.nil?
        params = object.parameters
        if object.has_tag?(:yield) || object.has_tag?(:yieldparam)
          params.reject! do |param|
            param[0].to_s[0, 1] == "&" &&
              !object.tags(:param).any? {|t| t.name == param[0][1..-1] }
          end
        end

        if params.empty?
          ""
        else
          args = params.map do |n, v|
            v ? "#{n}#{n[-1, 1] == ':' ? '' : ' ='} #{v}" : n.to_s
          end.join(", ")
          h("(#{args})")
        end
      end
```

