#!/bin/bash
cd ~/Code-Steel\ \(ORG\)/FORMALIZE.prj

report="Progress Reports/$(date +%m\ %B)/$(date +%d,\ %A)"
yesterday_report="Progress Reports/$(date -d 'yesterday' +%m\ %B)/$(date -d 'yesterday' +%d,\ %A)"
home="../../"
yesterday_output="$home/Code-White (INTRA)/RECORD.rou/Output/$(date -d 'yesterday' +%m\ %B)/$(date -d 'yesterday' +%d,\ %A)"

if [ ! -f "$report.lyx" ]; then
    if [ ! -d "Progress Reports/$(date +%m\ %B)" ]; then
       mkdir "Progress $Reports/(date +%m\ %B)"
    fi
    cat ~/.lyx/templates/Report.lyx > "$report.lyx"
    echo created report

    case $(date +%d | tail -c2) in
        1)
            suffix="st"
            ;;
        2)
            suffix="nd"
            ;;
        3)
            suffix="rd"
            ;;
        *)
            suffix="th"
    esac

    sed -i "$(awk '/June 29/{print NR; exit}' ~/.lyx/templates/Report.lyx) c\ $(date +%A,\ %B\ %-d$suffix,\ %Y)" "$report.lyx"
    echo named date
    lyx -e pdf "$report.lyx"
    echo compiled pdf
else
    echo file exists
fi

lyx -r "$report.lyx"  Classify/ObjectClasses.lyx Lawbook/Lawbook.lyx Lawbook/Pending\ Enactment.lyx Lawbook/Pending\ Approval.lyx &
okular "$yesterday_output.pdf" "$yesterday_report.pdf" "$report.pdf" Classify/ObjectClasses.pdf Lawbook/Lawbook.pdf Lawbook/Pending\ Enactment.pdf Lawbook/Pending\ Approval.pdf &
