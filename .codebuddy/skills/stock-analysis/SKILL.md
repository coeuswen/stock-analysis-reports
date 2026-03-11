---
name: stock-analysis
description: Analyze Chinese stock market daily review data including limit-up stocks and hot sector data. This skill should be used when the user requests stock market analysis based on daily data files (ztbYYYYMMDD.xlsx for limit-up stocks, rdfxYYYYMMDD.xlsx for hot sectors). The skill provides a complete workflow from data extraction to comprehensive HTML report generation with sector ranking, event analysis, and industry chain mining.
---

# Stock Analysis Skill

## Purpose

Analyze Chinese A-share market daily review data to identify hot sectors, track limit-up stocks, analyze driving events, and mine investment opportunities through industry chain logic. Generate professional HTML reports with stock code formatting, sector ranking, event timeline analysis, and investment strategy recommendations.

## When to Use This Skill

Use this skill when:
- User requests analysis of stock market daily review data
- User provides a date (e.g., "analyze 2026-03-11", "analyze today")
- User mentions "涨停", "热点板块", "复盘", or similar stock analysis terms
- Data files exist in the workspace with naming convention: `ztbYYYYMMDD.xlsx` and `rdfxYYYYMMDD.xlsx`

## Workflow

### Step 1: Data Extraction and Formatting

1. **Locate data files**: Find `ztbYYYYMMDD.xlsx` and `rdfxYYYYMMDD.xlsx` in the workspace
2. **Load data**: Use pandas to read Excel files
3. **Format stock codes**: Ensure all stock codes are 6-digit format using `.zfill(6)` method
4. **Save formatted data**: Create `ztbYYYYMMDD_formatted.xlsx` with properly formatted codes

Example code for formatting:
```python
# Format stock codes to 6 digits
ztb_df['股票代码'] = ztb_df['股票代码'].astype(str).str.zfill(6)
```

### Step 2: Sector Ranking Analysis

1. **Group by sector**: Count limit-up stocks per sector from hot sector data
2. **Rank sectors**: Sort by count descending and identify top 3 sectors
3. **List stocks**: For each top sector, list all limit-up stocks with:
   - Stock name
   - Stock code (6-digit format)
   - Limit-up reason
   - Consecutive limit-up count
   - Limit-up price
   - Percentage gain

### Step 3: Event Analysis and Sustainability

For each top 3 sectors, perform web searches to:
1. **Find event origin**: Search for the driving event mentioned in "热点分析" column
2. **Identify timeline**: Determine the start date of the event
3. **Analyze sustainability**: Classify event duration into:
   - Short-term (1-3 months)
   - Medium-term (3-6 months)
   - Long-term (1-3 years)
4. **Provide reasoning**: Explain why the event has sustained or declining momentum

Search patterns:
- Use specific sector names + event keywords
- Include year and month for temporal relevance
- Search for "持续性", "利好", "后续" terms

### Step 4: Industry Chain Mining

For top 2 sectors, conduct deep industry chain analysis:

#### 4.1 Identify Industry Chain Segments

- **Upstream**: Raw materials, equipment, core components
- **Midstream**: Manufacturing, processing, integration
- **Downstream**: Applications, services, end users
- **Related segments**: Supporting industries, derivative products

#### 4.2 Search for Beneficial Sectors

1. **Identify related sectors**: Search for sectors related to the main theme
2. **Search for beneficiary stocks**: Find stocks that benefit but haven't surged yet
3. **Prioritize stocks**: Focus on stocks that:
   - Have recent limit-up history
   - Show potential but not yet significant gains
   - Belong to related industry chains

Search patterns:
- Main sector + "产业链" + "受益股"
- Related sector names + "利好" + "涨停"
- Industry chain segments + "补涨" + "机会"

#### 4.3 Analyze Investment Logic

For each recommended sector and stock:
- Explain the connection to the main theme
- Identify the driving factors
- Assess growth potential
- Note current market status (limit-up, not limit-up, previous limit-up)

### Step 5: Report Generation

Generate a professional HTML report with:

#### 5.1 Visual Design Elements

- **Color scheme**: Use thematic colors for different sectors
  - Oil/Chemical: Red theme (#e74c3c)
  - Smart Grid: Blue theme (#3498db)
  - Photovoltaic: Green theme (#27ae60)
- **Gradient backgrounds**: Purple-blue gradients for headers
- **Card effects**: 3D shadow effects for containers
- **Interactive elements**: Hover effects for tables and navigation

#### 5.2 Content Structure

1. **Title Page**: Date, analysis overview
2. **Table of Contents**: Clickable navigation to sections
3. **Top 3 Sectors Overview**:
   - Ranking (🥇🥈🥉 icons)
   - Sector name
   - Number of limit-up stocks
   - All limit-up stocks table (with 6-digit codes)
4. **Event Analysis** for each top 3 sector:
   - Driving event description
   - Event start date
   - Sustainability analysis with timeline
   - Reasoning for sustainability judgment
5. **Industry Chain Analysis** for top 2 sectors:
   - Industry chain map (upstream/midstream/downstream)
   - Beneficial sectors not yet surged
   - Recommended stocks with status indicators
   - Investment logic explanation
6. **Investment Strategy**:
   - Short-term opportunities (1-3 months)
   - Medium/long-term opportunities (1-3 years)
   - Risk warnings
7. **Conclusion**: Summary and recommendations

#### 5.3 HTML Format Requirements

- **Document type**: `<!DOCTYPE html>`
- **Character set**: `<meta charset="UTF-8">`
- **Responsive design**: Maximum width 1400px, centered
- **Font**: Microsoft YaHei (微软雅黑) for Chinese text
- **Code font**: Courier New for stock codes
- **Print optimization**: CSS `@media print` for PDF export
- **Interactive elements**: JavaScript for smooth scrolling and hover effects

#### 5.4 Stock Code Display

- **Always use 6-digit format**: e.g., "002455" not "2455"
- **Background styling**: Light gray background with rounded corners
- **Monospace font**: Courier New for alignment
- **Status badges**:
  - Red badge (⚠️ 未涨停): Not limit-up yet
  - Green badge (✅ 已涨停): Currently limit-up
  - Blue badge (⚡ 前期涨停后回调): Previous limit-up, now corrected
  - Yellow badge (⚠️ 未涨停): Not limit-up but potential

#### 5.5 Table Design

- **Header row**: Gradient background (#667eea → #764ba2), white bold text
- **Odd rows**: Light gray background (#f8f9fa)
- **Even rows**: White background
- **Hover effect**: Light blue background (#e8f4f8), transform scale(1.01)
- **Transition**: 0.3s smooth animation
- **Borders**: Clear cell separation with padding

### Step 6: Report Presentation

After generating the HTML report:
1. **Save file**: Use naming convention `股票复盘分析报告_YYYYMMDD_超级精美版.html`
2. **Preview report**: Use `open_result_view` tool to display in browser
3. **Guide user**: Provide instructions for saving as PDF if needed
4. **Clean up**: Remove temporary Python scripts used for analysis

## Reusable Assets

### Scripts

Include the following Python scripts in the `scripts/` directory:

1. **format_codes.py**: Format stock codes to 6 digits
   - Reads `ztbYYYYMMDD.xlsx`
   - Formats stock codes using `.zfill(6)`
   - Saves to `ztbYYYYMMDD_formatted.xlsx`

2. **analyze_stocks.py**: Main analysis script
   - Reads formatted data
   - Performs sector ranking
   - Generates HTML report
   - Creates report file with proper naming

### References

Include the following reference documents in the `references/` directory:

1. **data_format.md**: Data file format documentation
   - Excel file structure
   - Column descriptions for ztb and rdfx files
   - Stock code format requirements

2. **industry_chains.md**: Industry chain reference data
   - Common sector industry chains
   - Upstream/midstream/downstream classifications
   - Related sectors mapping

3. **search_patterns.md**: Web search patterns for event analysis
   - Event search templates
   - Sustainability analysis keywords
   - Industry chain search strategies

## Best Practices

1. **Always format stock codes**: Never skip the 6-digit formatting step
2. **Verify data integrity**: Check that data files exist before processing
3. **Use specific search terms**: Include dates and sector names for accurate search results
4. **Prioritize recent limit-ups**: Focus on stocks with recent limit-up history
5. **Provide clear reasoning**: Explain investment logic for each recommendation
6. **Maintain visual consistency**: Use the same color scheme and design elements throughout the report
7. **Test report rendering**: Verify HTML displays correctly before presenting to user
8. **Optimize for PDF**: Ensure print CSS is properly configured

## Error Handling

- **File not found**: Check if data files exist with correct naming convention
- **Stock code formatting**: Handle cases where stock codes are already formatted
- **Empty data**: Handle cases with no limit-up stocks or hot sectors
- **Search failures**: Provide fallback analysis when web searches fail
- **Code execution**: Test Python scripts before full execution

## Output Format

The final output should be:
1. **HTML report**: Beautifully formatted with professional design
2. **Previewed in browser**: Using `open_result_view` tool
3. **Ready for PDF export**: Optimized for print-to-PDF
4. **Clean workspace**: Temporary scripts removed after completion
