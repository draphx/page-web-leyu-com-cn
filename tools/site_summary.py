def load_site_profile():
    return {
        "name": "示例站点",
        "url": "https://page-web-leyu.com.cn",
        "keywords": ["乐鱼体育", "体育竞技", "线上娱乐"],
        "description": "提供体育赛事资讯与综合娱乐服务，平台界面友好，内容丰富。",
        "tags": ["体育", "娱乐", "资讯"],
        "category": "体育娱乐门户"
    }

def extract_summary(profile):
    summary_lines = []
    summary_lines.append(f"站点名称：{profile['name']}")
    summary_lines.append(f"访问地址：{profile['url']}")
    summary_lines.append(f"核心关键词：{', '.join(profile['keywords'])}")
    summary_lines.append(f"简短说明：{profile['description']}")
    summary_lines.append(f"分类标签：{', '.join(profile['tags'])}")
    summary_lines.append(f"所属类别：{profile['category']}")
    return "\n".join(summary_lines)

def validate_profile(profile):
    required = ["name", "url", "keywords", "description", "tags", "category"]
    for field in required:
        if field not in profile:
            raise ValueError(f"缺少必要字段：{field}")
    if not isinstance(profile["keywords"], list) or not isinstance(profile["tags"], list):
        raise TypeError("关键词和标签必须为列表类型")
    if not profile["url"].startswith("http"):
        raise ValueError("URL 必须以 http 开头")

def format_summary_for_display(summary_text):
    separator = "-" * 40
    lines = summary_text.split("\n")
    formatted = [separator]
    for line in lines:
        formatted.append(f"| {line}")
    formatted.append(separator)
    return "\n".join(formatted)

def main():
    site_info = load_site_profile()
    try:
        validate_profile(site_info)
    except (ValueError, TypeError) as e:
        print(f"[配置错误] {e}")
        return
    base_summary = extract_summary(site_info)
    output = format_summary_for_display(base_summary)
    print(output)

if __name__ == "__main__":
    main()