#!/bin/bash

report="$REPORT/$(date +%m\ %B)/$(date +%d,\ %A)"
yesterday_report="$REPORT/$(date -d 'yesterday' +%m\ %B)/$(date -d 'yesterday' +%d,\ %A)"
home="../../"
yesterday_output="$home/Code-White (INTRA)/RECORD.rou/Output/$(date -d 'yesterday' +%m\ %B)/$(date -d 'yesterday' +%d,\ %A)"


if [ ! -f "$report.lyx" ]; then
    if [ ! -d "$REPORT/$(date +%m\ %B)" ]; then
       mkdir "$REPORT/(date +%m\ %B)"
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

cd ~/Code-Steel\ \(ORG\)/LAWBOOK.prj

lyx -r "$report.lyx"  ObjectClasses.lyx Lawbook.lyx Pending\ Enactment.lyx Pending\ Approval.lyx &
okular "$yesterday_output.pdf" "$yesterday_report.pdf" "$report.pdf" ObjectClasses.pdf Lawbook.pdf Pending\ Enactment.pdf Pending\ Approval.pdf &
