#!/bin/env bash
cd ~/Code-Steel\ \(ORG\)/FORMALIZE.proj

report="Progress Reports/$(date +%m\ %B)/$(date +%d,\ %A)"
yesterday_report="Progress Reports/$(date -d 'yesterday' +%m\ %B)/$(date -d 'yesterday' +%d,\ %A)"
home="../../"
yesterday_output="$home/Code-White (INTRA)/RECORD.rou/Output/$(date -d 'yesterday' +%m\ %B)/$(date -d 'yesterday' +%d,\ %A)"
if [ ! -f "$report.lyx" ]; then
    cat ~/.lyx/templates/Report.lyx > "$report.lyx"

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

    sed -i "$(awk '/June 29/{print NR; exit}' .lyx/templates/Report.lyx) c\ $(date +%A,\ %B\ %d$suffix,\ %Y)" "$report.lyx"
    lyx -e pdf "$report.lyx"
fi

lyx -r "$report.lyx"  Classify/ObjectClasses.lyx Lawbook/Lawbook.lyx Lawbook/Pending\ Enactment.lyx Lawbook/Pending\ Approval.lyx &
okular "$yesterday_output.pdf" "$yesterday_report.pdf" "$report.pdf" Classify/ObjectClasses.pdf Lawbook/Lawbook.pdf Lawbook/Pending\ Enactment.pdf Lawbook/Pending\ Approval.pdf &
